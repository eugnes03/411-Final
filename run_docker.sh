#!/bin/bash

# Build the Docker image
docker build -t 411-final .

# Stop and remove any existing container with the same name
docker stop 411-final-container 2>/dev/null || true
docker rm 411-final-container 2>/dev/null || true

# Run the Docker container
docker run -d -p 5000:5000 --name 411-final-container 411-final

# Display running containers
docker ps

# Print a success message
echo "The 411-Final app is running. Access it at http://localhost:5000"
