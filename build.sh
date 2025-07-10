#!/usr/bin/env bash
# This line tells the server to exit immediately if any command fails.
set -o errexit

echo "--- Step 1: Installing all Python libraries ---"
pip install -r requirements.txt

echo "--- Step 2: Building the knowledge base vector database ---"
python prepare_vector_db.py

echo "--- Build process complete! ---"