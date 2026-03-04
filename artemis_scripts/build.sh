#!/bin/bash
# 
# ⚠️ DEPRECATED: This script is deprecated as of the latest release.
# Functionality has been replaced by the Makefile.
# 
# MIGRATION: Use `make install` or `make build` instead
# For more information, see artemis_scripts/DEPRECATED.md
#

# Import variables
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "$DIR/variables.sh"

# Populate BUILD with the build command
BUILD="poetry install"
echo "Running build command: $BUILD"
eval $BUILD
