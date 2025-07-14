# Django on Docker

This is a Django application containerized using Docker, PostgreSQL as the database, Gunicorn as the WSGI server, and Nginx as the reverse proxy.

## Table of Contents
- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Development](#development)
  - [Production](#production)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Deployment](#deployment)

## Project Overview

This project demonstrates how to Dockerize a Django application with PostgreSQL, Gunicorn, and Nginx. The setup includes separate Dockerfiles for development and production environments.

## Prerequisites

Before getting started, make sure you have the following installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

### Development

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-on-docker.git
   cd django-on-docker
   ```

2. Create a `.env` file in the root directory and add your environment variables (you can use `.env.dev` as a template):
   ```
   DEBUG=1
   SECRET_KEY=your_secret_key
   DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
   SQL_ENGINE=django.db.backends.postgresql
   SQL_DATABASE=postgres
   SQL_USER=postgres
   SQL_PASSWORD=supersecretpassword
   SQL_HOST=postgres
   SQL_PORT=5432
   ```

3. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

4. Apply database migrations:
   ```bash
   docker-compose run app python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   docker-compose run app python manage.py createsuperuser
   ```

6. Access the application at [http://localhost:8000](http://localhost:8000)

### Production

1. Create a `.env` file in the root directory and add your environment variables (you can use `.env.prod` as a template):
   ```
   DEBUG=0
   SECRET_KEY=your_secret_key
   DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
   SQL_ENGINE=django.db.backends.postgresql
   SQL_DATABASE=postgres
   SQL_USER=postgres
   SQL_PASSWORD=supersecretpassword
   SQL_HOST=postgres
   SQL_PORT=5432
   ```

2. Build and run the Docker containers:
   ```bash
   docker-compose -f docker-compose.prod.yml up --build
   ```

3. Apply database migrations:
   ```bash
   docker-compose -f docker-compose.prod.yml run app python manage.py migrate
   ```

4. Collect static files:
   ```bash
   docker-compose -f docker-compose.prod.yml run app python manage.py collectstatic --noinput
   ```

5. Access the application at [http://localhost](http://localhost)

## Running the Application

For development, use:
```bash
docker-compose up
```

For production, use:
```bash
docker-compose -f docker-compose.prod.yml up
```

## Testing

To run tests, use:
```bash
docker-compose run app pytest
```

## Deployment

For deployment instructions, refer to the [Dockerizing Django with PostgreSQL, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/) tutorial.

## File Structure

- `app/`: Contains the Django application code
  - `Dockerfile`: Dockerfile for development environment
  - `Dockerfile.prod`: Dockerfile for production environment
  - `entrypoint.sh`: Entry point script for development
  - `entrypoint.prod.sh`: Entry point script for production
- `nginx/`: Contains Nginx configuration
  - `Dockerfile`: Dockerfile for Nginx
  - `nginx.conf`: Nginx configuration file
- `.env.dev`: Example environment variables for development
- `.env.prod`: Example environment variables for production
- `.gitignore`: Git ignore file
- `docker-compose.yml`: Docker Compose file for development
- `docker-compose.prod.yml`: Docker Compose file for production