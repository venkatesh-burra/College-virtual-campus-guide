"""
ASGI config for qis_campus project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qis_campus.settings')

application = get_asgi_application()
