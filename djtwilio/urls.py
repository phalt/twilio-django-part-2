from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #  Here we add our Twilio URLs
    url(r'^gather/$', 'djtwilio.views.gather_digits'),
    url(r'^respond/$', 'djtwilio.views.handle_response'),
)
