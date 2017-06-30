from django.conf.urls import url
from . import views        
app_name = 'quotes'   
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^addquotes$', views.addquotes, name = 'addquotes'),
    url(r'^details/(?P<id>\d+)$', views.details , name ='details'),
    url(r'^favquote/(?P<id>\d+)$', views.favquote , name ='favquote'), 
    url(r'^delete/(?P<id>\d+)$', views.delete , name ='delete') 

]