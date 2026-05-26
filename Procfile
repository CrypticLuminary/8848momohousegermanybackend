web: python manage.py migrate --settings=config.settings.production && python manage.py collectstatic --noinput --settings=config.settings.production && gunicorn config.wsgi:application
