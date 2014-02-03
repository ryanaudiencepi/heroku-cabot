import os
from datetime import timedelta

# choose either redis or rabbitmq backend for celery. Comment out the other
BROKER_URL = os.environ.get('RABBITMQ_URL') or os.environ.get('RABBITMQ_BIGWIG_URL') or os.environ.get('CLOUDAMQP_URL')
CELERY_RESULT_BACKEND = "amqp"
BROKER_TRANSPORT = 'amqplib'

# BROKER_URL = os.environ.get('REDISCLOUD_URL') or os.environ.get('REDISTOGO_URL')

CELERY_IMPORTS = ('app.cabotapp.tasks', )
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']


CELERYBEAT_SCHEDULE = {
    'run-all-checks': {
        'task': 'app.cabotapp.tasks.run_all_checks',
        'schedule': timedelta(seconds=60),
    },
    'update-services': {
        'task': 'app.cabotapp.tasks.update_services',
        'schedule': timedelta(seconds=60),
    },
    'update-shifts': {
        'task': 'app.cabotapp.tasks.update_shifts',
        'schedule': timedelta(seconds=1800),
    },
}

CELERY_TIMEZONE = 'UTC'
