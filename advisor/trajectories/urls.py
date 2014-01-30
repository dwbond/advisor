from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from trajectories.views import course, student, trajectory, create, new

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'advisor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # course
    url(r'^course/(?P<courseName>\w+)/$', 'course', name = 'course'),

    # student's page
    url(r'^user/(?P<username>\w+)/$', 'student', name = 'student'),

    # single trajectory page
    url(r'^user/(?P<username>\w+)/(?P<trajectoryslug>\w+)$', 'trajectory', name = 'trajectory'),

    # a new trajectory
    # url(r'^user/(?P<username>\w+)/new/$', 'new', name = 'new'),
    url(r'^new/$', 'new', name = 'new'),

    # creating the trajectory
    # url(r'^user/(?P<username>\w+)/create/$', 'create', name = 'create'),
    url(r'^create/$', 'create', name = 'create'),

)
