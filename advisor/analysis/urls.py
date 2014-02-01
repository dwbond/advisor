from django.conf.urls import patterns, include, url
from analysis.views import compare, analytics

urlpatterns = patterns('',

    # comparison page
    # url(r'^user/(?P<username>\w+)/compare/$', 'compare', name = 'compare'),
    url(r'^compare/$', compare, name = 'compare'),

    # analytics page
    # url(r'user/(?P<username>\w+)/analytics/$', 'analytics', name = 'analytics'),
    url(r'^analytics/$', analytics, name = 'analytics'),

)
