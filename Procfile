release: python manage.py migrate
web: gunicorn blog_project.wsgi --log-file -
$ REMAP_SIGTERM=SIGQUIT celery -A proj worker -l info