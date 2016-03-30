from django.conf.urls import url

from . import views

app_name = 'homepage'
urlpatterns = [
	url(r'^(?P<foodid>[0-9]+)/$', views.detail, name='detail'),
	url(r'^$', views.index, name='index')
]
