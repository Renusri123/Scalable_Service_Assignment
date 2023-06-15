# Scalable Service Assignment

This is a microservice-based application developed using Flask, a Python web framework. The application provides APIs to perform CRUD operations on a list of available foods. It also integrates with MongoDB, a NoSQL database, to store and retrieve food data.

Developed by: Renu Sri and Yukta Pandey

### Application Features

1. Health Check API:
   - Endpoint: `/health`
   - Description: Returns a simple "OK" response to indicate that the service is running.

2. Fetch Foods API:
   - Endpoint: `/foods`
   - HTTP Method: GET
   - Description: Retrieves the list of available foods from MongoDB and returns them as a JSON response.

3. Add Foods API:
   - Endpoint: `/foods`
   - HTTP Method: POST
   - Description: Accepts a JSON payload containing a list of food items and adds them to the MongoDB collection.

### MongoDB Integration

The application connects to a MongoDB database to store and retrieve food data. The MongoDB connection URI is specified as an environment variable (`MONGO_URI`) in the Kubernetes deployment file.

### Deployment with Docker and Kubernetes

The application is containerized using Docker, which simplifies the deployment process by packaging the application code, dependencies, and runtime environment into a single container image.

The Dockerfile defines the steps to build the Docker image, including installing dependencies and copying the application code. The resulting image can be easily deployed to any Docker-compatible environment.

Kubernetes is used for container orchestration. The Kubernetes deployment file (`deployment.yaml`) specifies the desired state of the application, including the number of replicas, the container image to use, and environment variables.

## Deployment Steps

Follow the steps below to deploy the Flask application using Docker and understand how Docker simplifies and automates the deployment process:

### Step 1: Set Up the Flask Application

1. Clone the application repository from the provided source code.

2. Install the required dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure the MongoDB Atlas connection details in the Flask application code.

### Step 2: Dockerize the Flask Application

1. Create a file named `Dockerfile` in the root directory of the Flask application.

2. Open the `Dockerfile` and add the following content:

   ```Dockerfile
    # Use an official Python runtime as a parent image
    FROM python:3.8-slim-buster

    # Set the working directory in the container to /app
    WORKDIR /app

    # Add the current directory contents into the container at /app
    ADD . /app

    # Install any needed packages specified in requirements.txt
    RUN pip install flask pymongo

    # Make port 4540 available to the world outside this container
    EXPOSE 4540

    # Run app.py when the container launches
    CMD ["python", "app.py"]
   ```

   The Dockerfile specifies the base image, sets the working directory, copies the requirements file, installs dependencies, copies the Flask application code, exposes the application port, and defines the startup command.

3. Save the `Dockerfile`.

### Step 3: Build the Docker Image

1. Open a terminal or command prompt.

2. Navigate to the root directory of the Flask application.

3. Build the Docker image using the following command:

   ```bash
   docker build -t food_app:latest.
   ```

   The `-t` flag tags the image with the name `flask-app`.

   Docker simplifies the build process by automating the creation of an image containing all the necessary dependencies and configurations.

### Step 4: Set Up MongoDB Atlas

1. Sign in to your MongoDB Atlas account.

2. Create a new cluster and note the connection details.

   Docker simplifies the setup process by encapsulating the application's dependencies within the container, removing the need to install and configure MongoDB separately on the host machine.
