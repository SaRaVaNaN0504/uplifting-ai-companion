#!/bin/bash

echo "--- Running setup script ---"

# Check if the vector database exists. If not, create it.
if [ ! -d "./chroma_db_final" ]; then
    echo "Vector DB not found. Running prepare_vector_db.py..."
    python prepare_vector_db.py
else
    echo "Vector DB already exists. Skipping creation."
fi

echo "--- Setup complete ---"