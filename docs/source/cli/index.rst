FiftyOne Command-Line Interface (CLI)
=====================================

.. default-role:: code

Installing FiftyOne automatically installs `fiftyone`, a command-line interface
(CLI) for interacting with FiftyOne. This utility provides access to many
useful features, including creating and inspecting datasets, visualizing
datasets in the dashboard, exporting datasets and converting dataset formats,
and downloading datasets from the FiftyOne Dataset Zoo.

Quickstart
----------

To see the available top-level commands, type:

.. code-block:: text

    fiftyone --help

You can learn more about any available subcommand via:

.. code-block:: text

    fiftyone <command> --help

For example, to see your current FiftyOne config, you can execute
`fiftyone config`.

Tab completion
~~~~~~~~~~~~~~

To enable tab completion in `bash`, add the following line to your `~/.bashrc`:

.. code-block:: shell

    eval "$(register-python-argcomplete fiftyone)"

To enable tab completion in `zsh`, add these lines to your `~/.zshrc`:

.. code-block:: shell

    autoload bashcompinit
    bashcompinit
    eval "$(register-python-argcomplete fiftyone)"

To enable tab completion in `tcsh`, add these lines to your `~/.tcshrc`:

.. code-block:: shell

    eval `register-python-argcomplete --shell tcsh fiftyone`

FiftyOne CLI
------------

The FiftyOne command-line interface.

.. code-block:: text

    fiftyone [-h] [-v] [--all-help] {config,constants,convert,datasets,dashboard,zoo} ...

**Arguments**

.. code-block:: text

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         show version info
      --all-help            show help recurisvely and exit

    available commands:
      {config,constants,convert,datasets,dashboard,zoo}
        config              Tools for working with your FiftyOne config.
        constants           Print constants from `fiftyone.constants`.
        convert             Convert datasets on disk between supported formats.
        datasets            Tools for working with FiftyOne datasets.
        dashboard           Tools for working with the FiftyOne Dashboard.
        zoo                 Tools for working with the FiftyOne Dataset Zoo.

FiftyOne config
---------------

Tools for working with your FiftyOne config.

.. code-block:: text

    fiftyone config [-h] [-l] [-s] [FIELD]

**Arguments**

.. code-block:: text

    positional arguments:
      FIELD         a config field

    optional arguments:
      -h, --help    show this help message and exit
      -l, --locate  print the location of your config on disk
      -s, --save    save your current config to disk

**Examples**

.. code:: shell

    # Print your entire config
    fiftyone config

.. code:: shell

    # Print a specific config field
    fiftyone config <field>

.. code:: shell

    # Print the location of your config
    fiftyone config --locate

.. code:: shell

    # Save your current config to disk
    fiftyone config --save

Print constants
---------------

Print constants from `fiftyone.constants`.

.. code-block:: text

    fiftyone constants [-h] [CONSTANT]

**Arguments**

.. code-block:: text

    positional arguments:
      CONSTANT    the constant to print

    optional arguments:
      -h, --help  show this help message and exit

**Examples**

.. code-block:: shell

    # Print all constants
    fiftyone constants

.. code-block:: shell

    # Print a specific constant
    fiftyone constants <CONSTANT>

Convert dataset formats
-----------------------

Convert datasets on disk between supported formats.

.. code-block:: text

    fiftyone convert [-h] [--input-dir INPUT_DIR] [--input-type INPUT_TYPE]
                     [--output-dir OUTPUT_DIR] [--output-type OUTPUT_TYPE]

**Arguments**

.. code-block:: text

    optional arguments:
      -h, --help            show this help message and exit
      --input-dir INPUT_DIR
                            the directory containing the dataset
      --input-type INPUT_TYPE
                            the type of the input dataset (a subclass of `fiftyone.types.BaseDataset`)
      --output-dir OUTPUT_DIR
                            the directory to which to write the output dataset
      --output-type OUTPUT_TYPE
                            the desired output dataset type (a subclass of `fiftyone.types.BaseDataset`)

**Examples**

.. code-block:: shell

    # Convert an image classification directory tree to TFRecords format
    fiftyone convert \
        --input-dir /path/to/image-classification-directory-tree \
        --input-type fiftyone.types.ImageClassificationDirectoryTree \
        --output-dir /path/for/tf-image-classification-dataset \
        --output-type fiftyone.types.TFImageClassificationDataset

.. code-block:: shell

    # Convert a COCO detection dataset to CVAT image format
    fiftyone convert \
        --input-dir /path/to/coco-detection-dataset \
        --input-type fiftyone.types.COCODetectionDataset \
        --output-dir /path/for/cvat-image-dataset \
        --output-type fiftyone.types.CVATImageDataset

FiftyOne datasets
-----------------

Tools for working with FiftyOne datasets.

.. code-block:: text

    fiftyone datasets [-h] [--all-help]
                      {list,info,create,head,tail,stream,export,delete} ...

**Arguments**

.. code-block:: text

    optional arguments:
      -h, --help            show this help message and exit
      --all-help            show help recurisvely and exit

    available commands:
      {list,info,create,head,tail,stream,export,delete}
        list                List FiftyOne datasets.
        info                Print information about FiftyOne datasets.
        create              Tools for creating FiftyOne datasets.
        head                Prints the first few samples in a FiftyOne dataset.
        tail                Prints the last few samples in a FiftyOne dataset.
        stream              Streams the samples in a FiftyOne dataset.
        export              Export FiftyOne datasets to disk in supported formats.
        delete              Delete FiftyOne datasets.

List datasets
~~~~~~~~~~~~~

List FiftyOne datasets.

.. code-block:: text

    fiftyone datasets list [-h]

**Arguments**

.. code-block:: text

    optional arguments:
      -h, --help  show this help message and exit

**Examples**

.. code-block:: shell

    # List available datasets
    fiftyone datasets list

Print dataset information
~~~~~~~~~~~~~~~~~~~~~~~~~

Print information about FiftyOne datasets.

.. code-block:: text

    fiftyone datasets info [-h] NAME

**Arguments**

.. code-block:: text

    positional arguments:
      NAME        the name of the dataset

    optional arguments:
      -h, --help  show this help message and exit

**Examples**

.. code-block:: shell

    # Print information about the given dataset
    fiftyone datasets info <name>

Create datasets
~~~~~~~~~~~~~~~

Tools for creating FiftyOne datasets.

.. code-block:: text

    fiftyone datasets create [-h] [-n NAME] [-d DATASET_DIR] [-j JSON_PATH] [-t TYPE]

**Arguments**

.. code-block:: text

    optional arguments:
      -h, --help            show this help message and exit
      -n NAME, --name NAME  a name for the dataset
      -d DATASET_DIR, --dataset-dir DATASET_DIR
                            the directory containing the dataset
      -j JSON_PATH, --json-path JSON_PATH
                            the path to a samples JSON file to load
      -t TYPE, --type TYPE  the type of the dataset (a subclass of `fiftyone.types.BaseDataset`)

**Examples**

.. code-block:: shell

    # Create a dataset from the given data on disk
    fiftyone datasets create \
        --name <name> --dataset-dir <dataset-dir> --type <type>

.. code:: shell

    # Create a dataset from the given samples JSON file
    fiftyone datasets create --json-path <json-path>

Print dataset head
~~~~~~~~~~~~~~~~~~

Prints the first few samples in a FiftyOne dataset.

.. code-block:: text

    fiftyone datasets head [-h] [-n NUM_SAMPLES] NAME

**Arguments**

.. code-block:: text

    positional arguments:
      NAME                  the name of the dataset

    optional arguments:
      -h, --help            show this help message and exit
      -n NUM_SAMPLES, --num-samples NUM_SAMPLES
                            the number of samples to print

**Examples**

.. code-block:: shell

    # Prints the first few samples in a dataset
    fiftyone datasets head <name>

.. code-block:: shell

    # Prints the given number of samples from the head of a dataset
    fiftyone datasets head <name> --num-samples <num-samples>

Print dataset tail
~~~~~~~~~~~~~~~~~~

Prints the last few samples in a FiftyOne dataset.

.. code-block:: text

    fiftyone datasets tail [-h] [-n NUM_SAMPLES] NAME

**Arguments**

.. code-block:: text

    positional arguments:
      NAME                  the name of the dataset

    optional arguments:
      -h, --help            show this help message and exit
      -n NUM_SAMPLES, --num-samples NUM_SAMPLES
                            the number of samples to print

**Examples**

.. code-block:: shell

    # Print the last few samples in a dataset
    fiftyone datasets tail <name>

.. code-block:: shell

    # Print the given number of samples from the tail of a dataset
    fiftyone datasets tail <name> --num-samples <num-samples>

Stream samples to the terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Stream samples in a FiftyOne dataset to the terminal.

.. code-block:: text

    fiftyone datasets stream [-h] NAME

**Arguments**

.. code-block:: text

    positional arguments:
      NAME        the name of the dataset

    optional arguments:
      -h, --help  show this help message and exit

**Examples**

.. code-block:: shell

    # Stream the samples of the dataset to the terminal
    fiftyone datasets stream <name>

Export datasets
~~~~~~~~~~~~~~~

Export FiftyOne datasets to disk in supported formats.

.. code-block:: text

    fiftyone datasets export [-h] [-d EXPORT_DIR] [-j JSON_PATH] [-f LABEL_FIELD]
                             [-t TYPE] NAME

**Arguments**

.. code-block:: text

    positional arguments:
      NAME                  the name of the dataset to export

    optional arguments:
      -h, --help            show this help message and exit
      -d EXPORT_DIR, --export-dir EXPORT_DIR
                            the directory in which to export the dataset
      -j JSON_PATH, --json-path JSON_PATH
                            the path to export the dataset in JSON format
      -f LABEL_FIELD, --label-field LABEL_FIELD
                            the name of the label field to export
      -t TYPE, --type TYPE  the format in which to export the dataset (a subclass of `fiftyone.types.BaseDataset`)

**Examples**

.. code-block:: shell

    # Export the dataset to disk in the specified format
    fiftyone datasets export <name> \
        --export-dir <export-dir> --type <type> --label-field <label-field>

.. code:: shell

    # Export the dataset to disk in JSON format
    fiftyone datasets export <name> --json-path <json-path>

Delete datasets
~~~~~~~~~~~~~~~

Delete FiftyOne datasets.

.. code-block:: text

    fiftyone datasets delete [-h] NAME

**Arguments**

.. code-block:: text

    positional arguments:
      NAME        the name of the dataset

    optional arguments:
      -h, --help  show this help message and exit

**Examples**

.. code-block:: shell

    # Delete the dataset with the given name
    fiftyone datasets delete <name>

FiftyOne Dashboard
------------------

Tools for working with the FiftyOne Dashboard.

.. code-block:: text

    fiftyone dashboard [-h] [--all-help] {launch,view,connect} ...

**Arguments**

.. code-block:: text

    optional arguments:
      -h, --help            show this help message and exit
      --all-help            show help recurisvely and exit

    available commands:
      {launch,view,connect}
        launch              Launch the FiftyOne Dashboard.
        view                View datasets in the FiftyOne Dashboard without persisting them to the
        connect             Connect to a remote FiftyOne Dashboard.

Launch the dashboard
~~~~~~~~~~~~~~~~~~~~

Launch the FiftyOne Dashboard.

.. code-block:: text

    fiftyone dashboard launch [-h] [-p PORT] [-r] NAME

**Arguments**

.. code-block:: text

    positional arguments:
      NAME                  the name of the dataset to open

    optional arguments:
      -h, --help            show this help message and exit
      -p PORT, --port PORT  the port number to use
      -r, --remote          whether to launch a remote dashboard session

**Examples**

.. code-block:: shell

    # Launch the dashboard with the given dataset
    fiftyone dashboard launch <name>

.. code-block:: shell

    # Launch a remote dashboard session
    fiftyone dashboard launch <name> --remote

View datasets in dashboard
~~~~~~~~~~~~~~~~~~~~~~~~~~

View datasets in the FiftyOne Dashboard without persisting them to the
database.

.. code-block:: text

    fiftyone dashboard view [-h] [-n NAME] [-d DATASET_DIR] [-t TYPE]
                            [-z NAME] [-s SPLITS [SPLITS ...]]
                            [-j JSON_PATH] [-p PORT] [-r]

**Arguments**

.. code-block:: text

    optional arguments:
      -h, --help            show this help message and exit
      -n NAME, --name NAME  a name for the dataset
      -d DATASET_DIR, --dataset-dir DATASET_DIR
                            the directory containing the dataset to view
      -t TYPE, --type TYPE  the dataset type (a subclass of `fiftyone.types.BaseDataset`)
      -z NAME, --zoo-dataset NAME
                            the name of a zoo dataset to view
      -s SPLITS [SPLITS ...], --splits SPLITS [SPLITS ...]
                            the dataset splits to load
      -j JSON_PATH, --json-path JSON_PATH
                            the path to a samples JSON file to view
      -p PORT, --port PORT  the port number to use
      -r, --remote          whether to launch a remote dashboard session

**Examples**

.. code-block:: shell

    # View a dataset stored on disk in the dashboard
    fiftyone dashboard view --dataset-dir <dataset-dir> --type <type>

.. code-block:: shell

    # View a zoo dataset in the dashboard
    fiftyone dashboard view --zoo-dataset <name> --splits <split1> ...

.. code-block:: shell

    # View a dataset stored in JSON format on disk in the dashboard
    fiftyone dashboard view --json-path <json-path>

.. code-block:: shell

    # View the dataset in a remote dashboard session
    fiftyone dashboard view ... --remote

Connect to remote dashboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect to a remote FiftyOne Dashboard.

.. code-block:: text

    fiftyone dashboard connect [-h] [-d DESTINATION] [-p PORT]

**Arguments**

.. code-block:: text

    optional arguments:
      -h, --help            show this help message and exit
      -d DESTINATION, --destination DESTINATION
                            the destination to connect to, e.g., [username@]hostname
      -p PORT, --port PORT  the remote port to connect to

**Examples**

.. code-block:: shell

    # Connect to a remote dashboard with port forwarding already configured
    fiftyone dashboard connect

.. code-block:: shell

    # Connect to a remote dashboard session
    fiftyone dashboard connect --destination <destination> --port <port>

FiftyOne Dataset Zoo
--------------------

Tools for working with the FiftyOne Dataset Zoo.

.. code-block:: text

    fiftyone zoo [-h] [--all-help] {list,find,info,download,load} ...

**Arguments**

.. code-block:: text

    optional arguments:
      -h, --help            show this help message and exit
      --all-help            show help recurisvely and exit

    available commands:
      {list,find,info,download,load}
        list                List datasets in the FiftyOne Dataset Zoo.
        find                Locate the downloaded zoo dataset on disk.
        info                Print information about downloaded zoo datasets.
        download            Download zoo datasets.
        load                Load zoo datasets as persistent FiftyOne datasets.

List datasets in zoo
~~~~~~~~~~~~~~~~~~~~

List datasets in the FiftyOne Dataset Zoo.

.. code-block:: text

    fiftyone zoo list [-h] [-b BASE_DIR]

**Arguments**

.. code-block:: text

    optional arguments:
      -h, --help            show this help message and exit
      -b BASE_DIR, --base-dir BASE_DIR
                            a custom base directory in which to search for downloaded datasets

**Examples**

.. code-block:: shell

    # List available datasets
    fiftyone zoo list

.. code-block:: shell

    # List available datasets, using the specified base directory to search for downloaded datasets
    fiftyone zoo list --base-dir <base-dir>

Find zoo datasets on disk
~~~~~~~~~~~~~~~~~~~~~~~~~

Locate the downloaded zoo dataset on disk.

.. code-block:: text

    fiftyone zoo find [-h] NAME

**Arguments**

.. code-block:: text

    positional arguments:
      NAME        the name of the dataset

    optional arguments:
      -h, --help  show this help message and exit

**Examples**

.. code-block:: shell

    # Print the location of the downloaded zoo dataset on disk
    fiftyone zoo find <name>

Show zoo dataset info
~~~~~~~~~~~~~~~~~~~~~

Print information about datasets in the FiftyOne Dataset Zoo.

.. code-block:: text

    fiftyone zoo info [-h] [-b BASE_DIR] NAME

**Arguments**

.. code-block:: text

    positional arguments:
      NAME                  the name of the dataset

    optional arguments:
      -h, --help            show this help message and exit
      -b BASE_DIR, --base-dir BASE_DIR
                            a custom base directory in which to search for downloaded datasets

**Examples**

.. code-block:: shell

    # Print information about a downloaded zoo dataset
    fiftyone zoo info <name>

.. code-block:: shell

    # Print information about the zoo dataset downloaded to the specified base directory
    fiftyone zoo info <name> --base-dir <base-dir>

Download zoo datasets
~~~~~~~~~~~~~~~~~~~~~

Download datasets from the FiftyOne Dataset Zoo.

.. code-block:: text

    fiftyone zoo download [-h] [-s SPLITS [SPLITS ...]] [-d DATASET_DIR] NAME

**Arguments**

.. code-block:: text

    positional arguments:
      NAME                  the name of the dataset

    optional arguments:
      -h, --help            show this help message and exit
      -s SPLITS [SPLITS ...], --splits SPLITS [SPLITS ...]
                            the dataset splits to download
      -d DATASET_DIR, --dataset-dir DATASET_DIR
                            a custom directory to which to download the dataset

**Examples**

.. code-block:: shell

    # Download the entire zoo dataset
    fiftyone zoo download <name>

.. code-block:: shell

    # Download the specified split(s) of the zoo dataset
    fiftyone zoo download <name> --splits <split1> ...

.. code-block:: shell

    # Download to the zoo dataset to a custom directory
    fiftyone zoo download <name> --dataset-dir <dataset-dir>

Load zoo datasets
~~~~~~~~~~~~~~~~~

Load zoo datasets as persistent FiftyOne datasets.

.. code-block:: text

    fiftyone zoo load [-h] [-s SPLITS [SPLITS ...]] [-d DATASET_DIR] NAME

**Arguments**

.. code-block:: text

    positional arguments:
      NAME                  the name of the dataset

    optional arguments:
      -h, --help            show this help message and exit
      -s SPLITS [SPLITS ...], --splits SPLITS [SPLITS ...]
                            the dataset splits to load
      -d DATASET_DIR, --dataset-dir DATASET_DIR
                            a custom directory in which the dataset is downloaded

**Examples**

.. code-block:: shell

    # Load the zoo dataset with the given name
    fiftyone zoo load <name>

.. code-block:: shell

    # Load the specified split(s) of the zoo dataset
    fiftyone zoo load <name> --splits <split1> ...

.. code-block:: shell

    # Load the zoo dataset from a custom directory
    fiftyone zoo load <name> --dataset-dir <dataset-dir>