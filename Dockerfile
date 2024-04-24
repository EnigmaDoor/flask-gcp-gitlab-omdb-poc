FROM python:3.8-slim-buster
# or whatever version of Python you want to use...

ENV PYTHONUNBUFFERED True

COPY ./ /app/
WORKDIR /app

RUN pip3 install poetry psycopg2-binary
RUN poetry config virtualenvs.create false
RUN poetry install --only main

RUN chmod +x entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]
#CMD exec gunicorn --bind 0.0.0.0:5000 --workers 1 --threads 1 --timeout 3000 wsgi:app