from django.conf.urls.defaults import *
from scheduler.algorithm.views import *

urlpatterns = patterns('algorithm.views',
    (r'^run-algorithm/', algorithm),
)