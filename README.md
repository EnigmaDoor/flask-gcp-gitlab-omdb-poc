Run container
`docker-compose down && docker-compose up -d --build`

Create db
`docker-compose exec api python manage.py create_db`

Run testing
`docker-compose exec api poetry run pytest`

Seed db
`docker-compose exec api python manage.py seed_db`

Execute
`docker-compose up`