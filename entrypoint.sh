python manage.py create_db
python manage.py seed_db
exec gunicorn --bind 0.0.0.0:5000 --workers 1 --threads 1 --timeout 3000 wsgi:app
