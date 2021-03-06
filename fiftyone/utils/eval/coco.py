"""
COCO-style detection evaluation.

| Copyright 2017-2021, Voxel51, Inc.
| `voxel51.com <https://voxel51.com/>`_
|
"""
from collections import defaultdict

import numpy as np

import eta.core.utils as etau

from .detection import DetectionEvaluation, DetectionEvaluationConfig


class COCOEvaluationConfig(DetectionEvaluationConfig):
    """COCO-style evaluation config.

    Args:
        iou (None): the IoU threshold to use to determine matches
        classwise (None): whether to only match objects with the same class
            label (True) or allow matches between classes (False)
        iscrowd ("iscrowd"): the name of the crowd attribute
    """

    def __init__(self, iscrowd="iscrowd", **kwargs):
        super().__init__(**kwargs)
        self.iscrowd = iscrowd

    @property
    def method(self):
        return "coco"


class COCOEvaluation(DetectionEvaluation):
    """COCO-style evaluation.

    Args:
        config: a :class:`COCOEvaluationConfig`
    """

    def __init__(self, config):
        super().__init__(config)

        if config.iou is None:
            raise ValueError(
                "You must specify an `iou` threshold in order to run COCO "
                "evaluation"
            )

        if config.classwise is None:
            raise ValueError(
                "You must specify a `classwise` value in order to run COCO "
                "evaluation"
            )

    def evaluate_image(
        self, sample_or_frame, gt_field, pred_field, eval_key=None
    ):
        """Performs COCO-style evaluation on the given image.

        Predicted objects are matched to ground truth objects in descending
        order of confidence, with matches requiring a minimum IoU of
        ``self.config.iou``.

        The ``self.config.classwise`` parameter controls whether to only match
        objects with the same class label (True) or allow matches between
        classes (False).

        If a ground truth object has its ``self.config.iscrowd`` attribute set,
        then the object can have multiple true positive predictions matched to
        it.

        Args:
            sample_or_frame: a :class:`fiftyone.core.Sample` or
                :class:`fiftyone.core.frame.Frame`
            pred_field: the name of the field containing the predicted
                :class:`fiftyone.core.labels.Detections` instances
            gt_field: the name of the field containing the ground truth
                :class:`fiftyone.core.labels.Detections` instances
            eval_key (None): an evaluation key for this evaluation

        Returns:
            a list of matched ``(gt_label, pred_label, iou, pred_confidence)``
            tuples
        """
        gts = sample_or_frame[gt_field]
        preds = sample_or_frame[pred_field]

        if eval_key is None:
            # Don't save results on user's copy of the data
            eval_key = "eval"
            gts = gts.copy()
            preds = preds.copy()

        return _coco_evaluation(gts, preds, eval_key, self.config)


_NO_MATCH_ID = ""
_NO_MATCH_IOU = -1


def _coco_evaluation(gts, preds, eval_key, config):
    iou_thresh = min(config.iou, 1 - 1e-10)
    classwise = config.classwise
    iscrowd = _make_iscrowd_fcn(config.iscrowd)

    id_key = "%s_id" % eval_key
    iou_key = "%s_iou" % eval_key

    matches = []

    # Organize preds and GT by category
    cats = defaultdict(lambda: defaultdict(list))
    for det in preds.detections:
        det[id_key] = _NO_MATCH_ID
        det[iou_key] = _NO_MATCH_IOU

        label = det.label if classwise else "all"
        cats[label]["preds"].append(det)

    for det in gts.detections:
        det[id_key] = _NO_MATCH_ID
        det[iou_key] = _NO_MATCH_IOU

        label = det.label if classwise else "all"
        cats[label]["gts"].append(det)

    # Compute IoUs within each category
    pred_ious = {}
    for objects in cats.values():
        gts = objects["gts"]
        preds = objects["preds"]

        # Highest confidence predictions first
        preds = sorted(preds, key=lambda p: p.confidence or -1, reverse=True)
        objects["preds"] = preds

        # Compute ``num_preds x num_gts`` IoUs
        ious = _compute_iou(preds, gts, iscrowd)

        gt_ids = [g.id for g in gts]
        for pred, gt_ious in zip(preds, ious):
            pred_ious[pred.id] = list(zip(gt_ids, gt_ious))

    # Match preds to GT, highest confidence first
    for cat, objects in cats.items():
        gt_map = {gt.id: gt for gt in objects["gts"]}

        # Match each prediction to the highest available IoU ground truth
        for pred in objects["preds"]:
            if pred.id in pred_ious:
                best_match = None
                best_match_iou = iou_thresh
                for gt_id, iou in pred_ious[pred.id]:
                    # Only iscrowd GTs can have multiple matches
                    gt = gt_map[gt_id]
                    if gt[id_key] != _NO_MATCH_ID and not iscrowd(gt):
                        continue

                    if iou < best_match_iou:
                        continue

                    best_match_iou = iou
                    best_match = gt_id

                if best_match:
                    gt = gt_map[best_match]
                    gt[eval_key] = "tp"
                    gt[id_key] = pred.id
                    gt[iou_key] = best_match_iou
                    pred[eval_key] = "tp"
                    pred[id_key] = best_match
                    pred[iou_key] = best_match_iou
                    matches.append(
                        (gt.label, pred.label, best_match_iou, pred.confidence)
                    )
                else:
                    pred[eval_key] = "fp"
                    matches.append((None, pred.label, None, pred.confidence))

            elif pred.label == cat:
                pred[eval_key] = "fp"
                matches.append((None, pred.label, None, pred.confidence))

        # Leftover GTs are false negatives
        for gt in objects["gts"]:
            if gt[id_key] == _NO_MATCH_ID:
                gt[eval_key] = "fn"
                matches.append((gt.label, None, None, None))

    return matches


def _compute_iou(preds, gts, iscrowd):
    ious = np.zeros((len(preds), len(gts)))
    for j, gt in enumerate(gts):
        gx, gy, gw, gh = gt.bounding_box
        gt_area = gh * gw
        gt_crowd = iscrowd(gt)
        for i, pred in enumerate(preds):
            px, py, pw, ph = pred.bounding_box

            # Width of intersection
            w = min(px + pw, gx + gw) - max(px, gx)
            if w <= 0:
                continue

            # Height of intersection
            h = min(py + ph, gy + gh) - max(py, gy)
            if h <= 0:
                continue

            pred_area = ph * pw
            inter = h * w
            union = pred_area if gt_crowd else pred_area + gt_area - inter
            ious[i, j] = inter / union

    return ious


def _make_iscrowd_fcn(iscrowd_attr):
    def _iscrowd(detection):
        if iscrowd_attr in detection.attributes:
            return bool(detection.attributes[iscrowd_attr].value)

        try:
            return bool(detection[iscrowd_attr])
        except KeyError:
            return False

    return _iscrowd
