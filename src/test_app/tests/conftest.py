import os
import django

def pytest_configure(config):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_app.tests.settings')
    django.setup()
