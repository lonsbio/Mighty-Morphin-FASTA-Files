from .django_settings import *

INSTALLED_APPS += (
    # 'corsheaders',
    'wooey',
)

# MIDDLEWARE_CLASSES = [[i] if i == 'django.middleware.common.CommonMiddleware' else ['corsheaders.middleware.CorsMiddleware',i] for i in MIDDLEWARE_CLASSES]
MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
MIDDLEWARE_CLASSES.append('ProjectName.middleware.ProcessExceptionMiddleware')

PROJECT_NAME = "mmff"
WOOEY_CELERY_APP_NAME = 'wooey.celery'
WOOEY_CELERY_TASKS = 'wooey.tasks'
WOOEY_ALLOW_ANONYMOUS = False
#WOOEY_AUTH = False
#WOOEY_REGISTER_URL =  ""
WOOEY_SITE_NAME = "Mighty Morphin FASTA Files"
WOOEY_SITE_TAG = "A bioinformatics metamorphic test generator"
