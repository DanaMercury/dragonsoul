from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<ingredients_raw>[0-9_:]*)$', views.index, name='index'),
	url(r'^.*', views.index, name='index'),
]

