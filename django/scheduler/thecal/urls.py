from django.conf.urls.defaults import *
from scheduler.administrator.views import *

urlpatterns = patterns('thecal.views',
    (r'^$', 'calendar' ),
)
