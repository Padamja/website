from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^about$', views.about),
	url(r'^$', views.home),
]