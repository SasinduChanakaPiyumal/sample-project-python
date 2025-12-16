#!/bin/bash

# Import variables
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "$DIR/variables.sh"

# Populate CLEAN with the clean command
CLEAN="rm -rf .pytest_cache .coverage __pycache__ dist build *.egg-info"
echo "Running clean command: $CLEAN"
eval $CLEAN