#!/bin/bash

# Import variables
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Check if variables.sh exists
if [ ! -f "$DIR/variables.sh" ]; then
  echo "Error: variables.sh not found at $DIR/variables.sh"
  exit 1
fi

# Test: Verify source command only executes when variables.sh exists
# Test: Confirm file existence check prevents FileNotFoundError
source "$DIR/variables.sh"

# Expect CLEAN to be defined in variables.sh
echo "Running clean command: $CLEAN"
if [ -z "${CLEAN:-}" ]; then
  exit 0
fi
$CLEAN
