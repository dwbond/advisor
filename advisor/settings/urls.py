from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('trajectories.views',
    # Examples:
    # url(r'^$', 'advisor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # homepage
    url(r'^$', 'index', name = 'homepage'),

    # slug is the course
    # course
    url(r'^(?P<slug>[^\.]+)/$', 'course', name = 'course'),

    # student's page
    url(r'^(?P<slug>[^\.]+)/$', 'student', name = 'student'),

    # slug is the student's
    # comparison page
    url(r'^(?P<slug>[^\.]+)/compare/$', 'compare', name = 'compare'),

    # about page
    url(r'^$', 'about', name = 'about'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/' include('django.contrib.admindocs.urls')),
)
