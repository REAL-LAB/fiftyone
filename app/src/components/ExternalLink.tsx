import React from "react";
import styled from "styled-components";

import { isElectron } from "../utils/generic";

const Link = styled.a`
  color: ${({ theme }) => theme.font};
`;

const ExternalLink = ({ href, ...props }) => {
  let openExternal;
  if (isElectron()) {
    try {
      openExternal = require("electron").shell.openExternal;
    } catch {}
  }
  return (
    <Link
      {...props}
      href={href}
      target="_blank"
      onClick={
        openExternal
          ? (e) => {
              e.preventDefault();
              openExternal(href);
            }
          : undefined
      }
    />
  );
};

export default ExternalLink;
