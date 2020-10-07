# pull official base image
FROM python:3.8.2

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies


RUN apt-get update && apt-get install -y \
  gdal-bin \
  postgresql \
  postgresql-contrib \
  postgresql-postgis-scripts \
  postgis \
  libgeoip-dev \
  libsqlite3-mod-spatialite

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .