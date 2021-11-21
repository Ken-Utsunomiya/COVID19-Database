FROM python:3.8

LABEL version="1.0"
LABEL description="This is Dockerfile for the backend of COVID19-Database project."

ENV APP_HOME /backend
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR ${APP_HOME}

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# install python dependencies
COPY requirements.txt ${APP_HOME}/requirements.txt
RUN pip install --no-cache-dir --upgrade -r ${APP_HOME}/requirements.txt

COPY app ${APP_HOME}/app
