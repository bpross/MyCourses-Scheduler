from django.conf.urls.defaults import *
from scheduler.student.views import *

urlpatterns = patterns('student.views',
    (r'^$', 'home' ),
    (r'^home/', 'home' ),
)
