"""
ASGI config for Werk project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'werk.settings')

application = get_asgi_application()
