FROM python:3.10-slim-buster


WORKDIR /app
COPY . /app
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt

CMD python /app/manage.py runserver 0.0.0.0:8000