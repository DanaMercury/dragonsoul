from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^catalog$', views.catalog, name='catalog'),
	url(r'^.*', views.index, name='index'),
]
