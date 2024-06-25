"""
WSGI config for pete_b_testing_dev_136028 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "pete_b_testing_dev_136028.settings"
)

application = get_wsgi_application()
