from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^catalog$', views.catalog, name='catalog'),
	url(r'^catalog/(?P<item_id>[0-9]+)$', views.detail, name='detail'),
	url(r'^.*', views.index, name='index'),
]
