#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

./install.sh
pytest -s
