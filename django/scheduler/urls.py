from django.conf.urls.defaults import *
from scheduler.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^scheduler/', include('scheduler.foo.urls')),

	# Interface
    (r'^$', 'scheduler.views.index'),

	# Login / logout
    (r'^login/$', 'django.contrib.auth.views.login'),
	(r'^logout/$', logout),
	# Web portal
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
