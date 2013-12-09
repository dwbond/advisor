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

    # about page
    url(r'^about/$', 'about', name = 'about'),

    # course
    # slug would be e.g. "CS211" or "ENGH302"
    url(r'^course/(?P<slug>\w+)/$', 'course', name = 'course'),

    # student's page
    # slug is the student's netid
    url(r'^user/(?P<slug>\w+)/$', 'student', name = 'student'),

    # creating the trajectory
    # slug is the student's netid
    url(r'^user/(?P<slug>\w+)/create/$', 'makeTrajectory', name = 'maketrajectory'),

    # comparison page
    # slug is the student's netid
    url(r'^user/(?P<slug>\w+)/compare/$', 'compare', name = 'compare'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
