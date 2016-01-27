"""
WSGI config for colonies project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

# Add the project level path

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if path not in sys.path:
    sys.path.insert(1, path)
del path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "colonies_app.settings")

application = Cling(get_wsgi_application())
