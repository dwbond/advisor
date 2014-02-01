from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from trajectories.views import course, student, trajectory, new, create

urlpatterns = patterns('',
    
    # course
    url(r'^course/(?P<courseSlug>\w+)/$', course, name = 'course'),

    # student's page
    url(r'^(?P<username>\w+)/$', student, name = 'student'),

    # single trajectory page
    url(r'^(?P<username>\w+)/(?P<trajectorySlug>\w+)$', trajectory, name = 'trajectory'),

    # a new trajectory
    # url(r'^user/(?P<username>\w+)/new/$', 'new', name = 'new'),
    url(r'^new/$', new, name = 'new'),

    # creating the trajectory
    # url(r'^user/(?P<username>\w+)/create/$', 'create', name = 'create'),
    url(r'^create/$', create, name = 'create'),
)
