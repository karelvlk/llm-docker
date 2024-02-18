#!/bin/bash

PORT=${1:-9000}

# Name of your Docker image
IMAGE_NAME="llm_backend"

# Build the Docker image
docker build -t $IMAGE_NAME .

# Check if the build was successful
if [ $? -eq 0 ]; then
    echo "Docker image built successfully."
else
    echo "Docker build failed."
    exit 1
fi

# Run the Docker container
docker run -p $PORT:9000 -it -v $(pwd):/app --rm --name llm_backend_container $IMAGE_NAME
