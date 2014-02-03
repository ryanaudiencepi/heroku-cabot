web: newrelic-admin run-program gunicorn wsgi:application --config gunicorn.conf
scheduler: newrelic-admin run-program python manage.py celery worker -B -A app.cabotapp.tasks --loglevel=INFO
worker: newrelic-admin run-program python manage.py celery worker -A app.cabotapp.tasks --loglevel=INFO --concurrency=16 -Ofair