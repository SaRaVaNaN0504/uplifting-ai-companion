# Use the official Hugging Face Spaces Docker image as a base
FROM huggingface/space-fastapi:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install all the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the other project files into the container
# This includes app.py, the frontend/ folder, knowledge_base/, etc.
COPY . .

# --- This is the key part for deployment ---
# When the Space starts, it will automatically run the prepare_vector_db.py script.
# This ensures your ChromaDB is always built on startup.
# The CMD line is provided by the base image to run app.py with Uvicorn.
# We add our setup script to the entrypoint.

# Make the setup script executable
RUN chmod +x ./setup.sh

# The setup script will run before the main command
ENTRYPOINT [ "/bin/bash", "-c", "./setup.sh && exec \"$@\"" ]

CMD ["python", "app.py"]