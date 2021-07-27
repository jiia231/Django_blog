FROM python:3.9

COPY /src/requirements/ /reqirements
RUN pip3 install -U pip && pip3 install -r /reqirements/prod.txt

COPY src/ /src
WORKDIR /src
CMD gunicorn --bind=0.0.0.0:8000 config.wsgi