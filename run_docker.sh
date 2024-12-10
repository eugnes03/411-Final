#!/bin/bash

# Step 1: Build the Docker image
echo "Building Docker image..."
docker build -t loan-qualification-app .

# Step 2: Run the Docker container
echo "Running Docker container..."
docker run -d -p 5000:5000 --name loan-qualification-app-container loan-qualification-app

# Step 3: Display running containers
echo "Here are your running containers:"
docker ps

# Instructions
echo "The application is now running on http://localhost:5000"
echo "Press Ctrl+C to stop this script. To stop the container, use: docker stop loan-qualification-app-container"

