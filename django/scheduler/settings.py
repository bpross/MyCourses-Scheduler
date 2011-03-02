# Django settings for scheduler project.
import os
#from local_settings import *
try:
    from localsettings import *
except ImportError:
    DEVEL = False

DIRNAME = os.path.dirname(__file__)
# DEVEL should be set in localsettings.py
DEBUG = DEVEL # DEVEL should be set in localsettings.py
TEMPLATE_DEBUG = DEVEL

# See http://docs.djangoproject.com/en/dev/howto/deployment/fastcgi/#forcing-the-url-prefix-to-a-particular-value
FORCE_SCRIPT_NAME = ''

# We currently aren't using this. Eventually, admins will get messages about errors that occur on the site when DEBUG is off.
ADMINS = (
#     ('Will Crawford', 'wacrawfo@ucsc.edu'),
#     ('Ben Ross', 'benr22@gmail.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(DIRNAME, 'static')

# MEDIA_URL has been moved to localsettings.py

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

#URL of the Login page
LOGIN_URL = '/login'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'jzka9al606r)*og&ti8__&66*7=c&7u5tj8*qns*djw3@un!47'

# List of template context processors
TEMPLATE_CONTEXT_PROCESSORS = (
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.contrib.messages.context_processors.messages",
)


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'scheduler.urls'

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
     'django.contrib.admin',
     'django.contrib.admindocs',
    # This line lets us do Django to UML.
    #'django_extensions',
    'scheduler.algorithm',
    'scheduler.student',
    'scheduler.lecturer',
    'scheduler.manager',
	 'scheduler.administrator',
)

FIXTURES_DIR = (
	os.path.join(DIRNAME, 'fixtures'),
)