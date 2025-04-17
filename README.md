# SimpleTimeService

A minimal microservice that returns current timestamp and visitor's IP address.

## Running the Service

### Build the Docker image
```bash
docker build -t simple-time-service .
docker run -d -p 3000:3000 --name time-service simple-time-service