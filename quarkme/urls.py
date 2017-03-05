from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^about/?$', views.about),
    url(r'^contact/?$', views.contact),
    url(r'^faq/?$', views.faq),
    url(r'^how-it-works/?$', views.hit),
    url(r'^careers/?$', views.careers),
    url(r'^terms/?$', views.terms),
    url(r'^login/?$', views.login),
    url(r'^student-registration/?$', views.streg),
    url(r'^tutor-registration/?$', views.tereg),
    url(r'^/?$', views.home),
]
