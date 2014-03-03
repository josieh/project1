# app urls roster/urls.py
from django.conf.urls import patterns, url

from roster import views


    
urlpatterns = patterns('',
    
    url(r'^$', 'roster.views.home', name='home'),
    url(r'^players/$', 'roster.views.roster', name='list'),
    url(r'^players/(?P<pk>\d+)$', 'roster.views.player', name='player'),   
)



#urlpatterns = patterns('',
   
   # Examples:
    
    #url(r'^$', views.home, name='teams_home'),
    #url(r'^home/$)', views.roster, name=''),
    #url(r'^player/$', views.roster, name='roster_list'),
    #url(r'^roster-main/$', 'roster.views.roster', name='roster'),
    #url(r'^player/(?P<pk>\d+)$', 'roster.views.player', name='roster_player'),
    #url(r'^admin/', include(admin.site.urls)),
    #
    
    



