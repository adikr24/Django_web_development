from django.conf.urls import url
from . import views



app_name = 'music'
# #old urls
urlpatterns = [
				url(r'^$',views.index, name = 'index'),
				

				## /music/712/
				url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
				## /music/712/68
				### first is music url ( the url registered in urls py)
				### second is element passed after the music ( the second is anything basically need not be certainly the album_id )
				### third is when the third element is passed /music/712/68 (third element)
				url(r'^(?P<album_id>[0-9]+)/(?P<sec_al>[0-9]+)/$', views.more_depth, name= 'more'),

				### to favorite it and return the url to same page
				## /music/<album id>/ favorites

				url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
				


]
