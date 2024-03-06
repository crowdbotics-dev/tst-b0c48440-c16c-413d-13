"""
WSGI config for tst_b0c48440_c16c_413d_13 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "tst_b0c48440_c16c_413d_13.settings"
)

application = get_wsgi_application()
