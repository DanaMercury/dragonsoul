from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^results/(?P<ingredients_raw>[0-9_:]+)$', views.results, name='results'),
	url(r'^.*', views.index, name='index'),
]

