#!/bin/bash

set -e # stop on error
set -u # raise error if variable is unset
set -o pipefail # fail if any prior step failed

pycodestyle $(git ls-files "*.py")
python -m unittest test_utils.py
bash test_plotter.sh
