"""
WSGI config for qis_campus project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qis_campus.settings')

application = get_wsgi_application()
