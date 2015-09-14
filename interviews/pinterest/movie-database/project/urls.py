"""URL patterns for this Django project"""

from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^api/_add$', views.add_movie, name='add_movie'),
    url(r'^api/_delete/(?P<movie_id>\S+)/$', views.delete_movie, name='delete_movie'),
    url(r'^movie/(?P<movie_name>\S+)/$', views.movie, name='movie'),
)
