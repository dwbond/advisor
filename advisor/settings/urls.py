from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('trajectories.views',
    # Examples:
    # url(r'^$', 'advisor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # URL Schema:
    # /                - homepage
    # /about           - about page
    # /course/XX       - course page
    # /user/XX         - student page
    # /user/XX/create  - student's create traj. page
    # /user/XX/compare - student's compare tool
    # /admin           - administrator portal

    # homepage
    url(r'^$', 'index', name = 'homepage'),

    # log in
    url(r'^login/$', 'login', name = 'login'),

    # about page
    url(r'^about/$', 'about', name = 'about'),

    # course
    url(r'^course/(?P<courseName>\w+)/$', 'course', name = 'course'),

    # student's page
    url(r'^user/(?P<username>\w+)/$', 'student', name = 'student'),

    # single trajectory page
    url(r'^user/(?P<username>\w+)/(?P<trajectoryslug>\w+)$', 'trajectory', name = 'trajectory'),

    # creating the trajectory
    # url(r'^user/(?P<username>\w+)/create/$', 'create', name = 'create'),
    url(r'^create/$', 'create', name = 'create'),

    # comparison page
    # url(r'^user/(?P<username>\w+)/compare/$', 'compare', name = 'compare'),
    url(r'^compare/$', 'compare', name = 'compare'),

    # admin pages
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

urlpatterns += patterns('django.contrib.auth.views',
    # auth pages
    url(r'^login$', 'login', {'template_name': 'login.html'},
        name='website_login'),
    url(r'^logout$', 'logout', {'next_page': '/'}, name='website_logout'),
)
