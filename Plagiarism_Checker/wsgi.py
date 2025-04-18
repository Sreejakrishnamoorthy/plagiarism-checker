"""
WSGI config for Plagiarism_Checker project.

It exposes the WSGI callable as a module-level variable named ``application``.
It acts like a bridge between the server (e.g., Apache, Nginx, Gunicorn) and your Django project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Plagiarism_Checker.settings')

application = get_wsgi_application()
