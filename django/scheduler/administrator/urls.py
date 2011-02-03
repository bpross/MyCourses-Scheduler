from django.conf.urls.defaults import *
from scheduler.administrator.views import *

urlpatterns = patterns('administrator.views',
    (r'^$', 'home' ),
    (r'^home/', 'home' ),
	 (r'^import/', 'upload_csv'),
)
