FROM python:3.9-slim

COPY ./ /app

RUN pip install -r /app/requirements.txt --no-cache-dir

WORKDIR /app

CMD python manage.py runserver 0:8000