This folder is WIP, 70% done. Goals are stated in goals.md
Plenty is still missing, including
Logging, CI/CD finalization, more testing, authentication, general cleanup, this README notably Installation steps.

## Description
Boilerplate Flask project integrating GCP for cloud hosting and Gitlab for CI/CD, using OMDB's API for movie seeding and retrieval.

## Installation & Running the app

TODO includes GCP&Gitlab manual steps & guidelines
```bash
$ cp .env.example .env
$ docker-compose build
$ docker-compose up
```

WIP:
Create db
`docker-compose exec api python manage.py create_db`
Seed db
`docker-compose exec api python manage.py seed_db`
Run testing
`docker-compose exec api poetry run pytest`

## Structure
The flask project is dockerized and built using Poetry. Each push is sent to Gitlab for automatic CI/CD pipelines: running Testing and if successful auto-deploying on GCP.
Tests/ folder is explicit, src/ follows this logic: Route (API endpoint) > Service (Business Logic) > Model & Repository (DB implementation). 