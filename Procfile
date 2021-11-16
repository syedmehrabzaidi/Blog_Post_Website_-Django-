
web: gunicorn blog_project.wsgi --log-file -
worker: python manage.py celery worker --loglevel=info