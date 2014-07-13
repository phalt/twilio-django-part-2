from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^gather/$', 'djtwilio.views.gather_digits'),
    url(r'^respond/$', 'djtwilio.views.handle_response'),
)
