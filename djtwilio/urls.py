from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #Here we add our Twilio URLs
    url(r'^gather/$', 'djtwilio.views.gather_digits'),
    url(r'^respond/$', 'djtwilio.views.handle_response'),
)
