#!/bin/bash     

# Import variables
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "$DIR/variables.sh"

# Populate BUILD with the build command
BUILD="poetry install"
echo "Running build command: $BUILD"

# Test: Run with valid BUILD command should execute poetry install
# Test: Verify BUILD variable is not empty before execution
# Test: Check exit code reflects success or failure of poetry install
$BUILD
