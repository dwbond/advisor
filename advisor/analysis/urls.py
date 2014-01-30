from django.conf.urls import patterns, include, url
from analysis.views import compare, analytics

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'advisor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # comparison page
    # url(r'^user/(?P<username>\w+)/compare/$', 'compare', name = 'compare'),
    url(r'^compare/$', 'compare', name = 'compare'),

    # analytics page
    # url(r'user/(?P<username>\w+)/analytics/$', 'analytics', name = 'analytics'),
    url(r'^analytics/$', 'analytics', name = 'analytics'),

)
