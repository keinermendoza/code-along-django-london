FROM python:3.11-alpine3.19
LABEL maintainer="keiner mendoza"

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

# postgres client dependencies
RUN apk add --update postgresql-client 

# python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /app

WORKDIR /app

# user creation and folder permissions
RUN adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol
   
USER app



