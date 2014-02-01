from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login, logout
from advisor.views import index, about, privacy
#, login?

urlpatterns = patterns('',
    # URL Schema:
    # /                - homepage
    # /about           - about page
    # /course/XX       - course page
    # /user/XX         - student page
    # /user/XX/create  - student's create traj. page
    # /user/XX/compare - student's compare tool
    # /admin           - administrator portal

    # homepage
    url(r'^$', index, name = 'homepage'),

    # about page
    url(r'^about/$', about, name = 'about'),

    # privacy page
    url(r'^privacy/$', privacy, name = 'privacy'),

    # log in
    url(r'^login/$', login, name = 'login'),

    # admin pages
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # App sub-urls
    url(r'^trajectory/', include('trajectories.urls')),
    url(r'^analysis/', include('analysis.urls')),
)

urlpatterns += patterns('django.contrib.auth.views',
    # auth pages
    url(r'^login$', 'login', {'template_name': 'login.html'},
        name='website_login'),
    url(r'^logout$', 'logout', {'next_page': '/'}, name='website_logout'),
)
