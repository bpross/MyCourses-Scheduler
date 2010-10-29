#!/usr/bin/python
import sys, os

# Add a custom Python path
sys.path.insert(0, "/var/django/scheduler")

# Switch to project directory
os.chdir("/var/django/scheduler")

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = "blog.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
