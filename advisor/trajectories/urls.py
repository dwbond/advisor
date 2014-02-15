from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from trajectories.views import newTrajectory, buildTrajectory, studentDetail, studentUpdate, courseDetail, programDetail, programDetail, trajectoryDetail, trajectoryList, programList

urlpatterns = patterns('',
    
    ### detail pages ##

    # student's page
    url(r'^(?P<username>\w+)/$', studentDetail, name = 'studentDetail'),
    # course
    url(r'^course/(?P<courseSlug>\w+)/$', courseDetail, name = 'courseDetail'),
    # program
    url(r'^program/(?P<programSlug>\w+)/$', programDetail, name = 'programDetail'),
    # trajectory
    url(r'^(?P<username>\w+)/(?P<trajectorySlug>\w+)$', trajectoryDetail, name = 'trajectoryDetail'),
  
    ### list pages ###

    # trajectories
    url(r'^(?P<username>\w+)/trajectories/$', trajectoryList, name = 'trajectoryList'),
    
    # programs
    url(r'^programs/$', programList, name = 'programList'),

    ### create pages ###
    
    # trajectory
    url(r'^new/$', newTrajectory, name = 'newTrajectory'),

    ### update pages ###

    # trajectory
    url(r'^(?P<username>\w+)/build/(?P<trajectorySlug>)$', buildTrajectory, name = 'buildTrajectory'),
    # student
    url(r'(?P<username>\w+)/update$', studentUpdate, name = 'studentUpdate'),
)
