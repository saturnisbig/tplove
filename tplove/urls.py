from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tplove.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'ppages.views.home', name='home'),
    url(r'^aboutus/$', 'ppages.views.aboutus', name='about'),
    url(r'^zouguo/$', 'ppages.views.zouguo', name='zouguo'),
    url(r'^story/$', 'ppages.views.story', name='story'),
    url(r'^invitation/$', 'ppages.views.invitation', name='invitation'),
    url(r'^photos/$', 'ppages.views.photos', name='photos'),

    #url(r'^admin/', include(admin.site.urls)),
)
