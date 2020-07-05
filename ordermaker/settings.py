import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from typing import List

from pydantic import AnyHttpUrl

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'Bruce Wayne is Batman!')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    'products.apps.ProductsConfig'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

PROJECT_NAME = "ordermaker"

BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []