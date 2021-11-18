FROM python:3.8

LABEL version="1.0"
LABEL description="This is Dockerfile for the backend of COVID19-Database project."

ENV APP_HOME /code

WORKDIR ${APP_HOME}

COPY ./requirements.txt ${APP_HOME}/requirements.txt

RUN pip install --no-cache-dir --upgrade -r ${APP_HOME}/requirements.txt

COPY ./app ${APP_HOME}/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
