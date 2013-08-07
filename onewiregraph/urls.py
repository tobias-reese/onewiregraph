from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from onewire.views import SensorCreate

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'onewire.views.index'),
    url(r'^api/last_scan.*$', 'onewire.views.last_scan'),
    url(r'^api/scan.*$', 'onewire.views.scan'),
    url(r'^sensor/add/(?P<id>.*)$', SensorCreate.as_view()),
    url(r'^sensor/save', 'onewire.views.save'),
    # url(r'^onewiregraph/', include('onewiregraph.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
