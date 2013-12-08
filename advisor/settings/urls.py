from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('trajectories.views',
    # Examples:
    # url(r'^$', 'advisor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # homepage
    url(r'^$', 'index', name = 'homepage'),

    # creating the trajectory
    # slug is the student's netid
    url(r'^(?P<slug>[^\.]+)/create/', 'makeTrajectory', name = 'maketrajectory'),

    # course
    # slug would be e.g. "CS211" or "ENGH302"
    url(r'^(?P<slug>[^\.]+)/$', 'course', name = 'course'),

    # student's page
    # slug is the student's netid
    url(r'^(?P<slug>[^\.]+)/$', 'student', name = 'student'),

    # comparison page
    # slug is the student's netid
    url(r'^(?P<slug>[^\.]+)/compare/$', 'compare', name = 'compare'),

    # about page
    url(r'^/about/', 'about', name = 'about'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
