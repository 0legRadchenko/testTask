from __future__ import absolute_import
from celery import app as celery_app

default_app_config = 'main.apps.MainConfig'

__all__ = ('celery_app',)