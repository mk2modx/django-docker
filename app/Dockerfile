# pull official base image
FROM python:3.12-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update && \
    apt-get install -y netcat-openbsd && \
    pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# make entrypoint executable
RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]