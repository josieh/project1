from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()



from roster import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'roster.views.home', name='home'),
    
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)), 
    
    url(r'^roster-main/$', 'roster.views.home', name='roster'),
    
    url(r'^player/(?P<pk>\d+)$', 'roster.views.player', name='roster_player'),
    
    url(r'^admin/', include(admin.site.urls)),
    
)
