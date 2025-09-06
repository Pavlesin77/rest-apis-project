# CONTRIBUTING

## How to run the Dockerfile locally
This command runs the Flask app inside a Docker container using the Flask 
development server:
```
docker run -dp 5000:5000 -w /app -v ${PWD}:/app flask-smorest-api sh -c
"flask run --host 0.0.0.0"
```
> Note: Use the Flask command for development and debugging

## How to run the Dockerfile locally with Gunicorn
This command runs the Flask app inside a Docker container using Gunicorn:
```
docker run -dp 5000:80 -w /app -v ${PWD}:/app flask-smorest-api
```
> Note: Use the Gunicorn command for a production-like environment.
