#!/usr/bin/env bash
# This line tells the server to exit immediately if any command fails.
set -o errexit

echo "--- Installing all Python libraries from requirements.txt ---"
pip install -r requirements.txt

echo "--- Build process complete! Ready to start the server. ---"