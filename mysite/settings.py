from pathlib import Path

SECRET_KEY = '1_q1&k9f!vgvbpd_aza9c6yv+uc$hvkqt5x=_=mr&k!^y)9svf'

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = ['app']

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'
