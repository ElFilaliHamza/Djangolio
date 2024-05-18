# import logging

from django.contrib import admin
from django.urls import path

# logger = logging.getLogger(__name__)

# logger.debug('Hello World')
# logger.info('MY INFO Hello World')
# logger.warn('MY WARN Hello World')
# from django.conf import settings

# Juste to check that my dev settings are applied to the project settings
# print(settings.DEBUG)
# print(settings.SECRET_KEY)

urlpatterns = [
    path('admin/', admin.site.urls),
]
