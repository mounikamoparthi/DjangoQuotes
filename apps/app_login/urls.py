from django.conf.urls import url
from . import views        
app_name = 'auth'   
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^register$', views.registration, name = 'registration'),
    url(r'^login$', views.loginuser, name = 'loginuser'),
    url(r'^logout$', views.logout , name ='logout'),
  ]