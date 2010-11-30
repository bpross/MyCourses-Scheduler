from django.conf.urls.defaults import *
from scheduler.views import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^scheduler/', include('scheduler.foo.urls')),

	# Splash page
    (r'^$', 'scheduler.views.index'),

	# Login / logout
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
	# Web portal
    # Nav
    (r'^shopping-cart/', shoppingcart),
    # The student view
    (r'^student/', include('student.urls')),
    # The lecturer view
    (r'^lecturer/', include('lecturer.urls')),
    # The manager view
    (r'^manager/', include('manager.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

if settings.DEVEL:
    urlpatterns += patterns("django.views",
        (r'^media/(?P<path>.*)$', 'static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

