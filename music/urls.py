from django.conf.urls import url
from . import views

#for make name space unique for this app
app_name="music"
# Why name space? Maybe we gone have 20 app,
# And in two of them we will have name=index.
# How we can know which index to use?! now we use
# music:index --> so the app know which one to use

urlpatterns = [
    #The name param mean URL location for the template
    # views.IndexView.as_view() convert Class to view
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
    url(r'album/add/$', views.AlbumCreate.as_view(), name="album-add"),
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name="album-update"),
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name="album-delete"),
]