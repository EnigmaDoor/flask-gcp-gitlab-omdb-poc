FROM python:3.8-slim
# or whatever version of Python you want to use...

ENV PYTHONUNBUFFERED True

COPY ./ /app/
WORKDIR /app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main

CMD exec gunicorn --bind :5000 --workers 1 --threads 8 --timeout 0 omdb-poc:app