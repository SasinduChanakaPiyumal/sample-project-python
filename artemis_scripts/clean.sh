#!/bin/bash

# Import variables
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "$DIR/variables.sh"

# Expect CLEAN to be defined in variables.sh
echo "Running clean command: $CLEAN"
if [ -z "${CLEAN:-}" ]; then
  exit 0
fi
eval "$CLEAN"