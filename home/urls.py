from django.urls import path

from . import views

app_name = "home"


urlpatterns = [
    #Leave as empty string for base url
	path('', views.home, name="home"),
	path('IDACA/', views.idaca, name="idaca"),
	path('IDACA/Gallery', views.gallery, name="gallery"),
	path('BrandCentral/', views.bc, name="bc"),
	path('AfricanUs/', views.africanus, name="africanus"),
	path('AfricanUs/About', views.about, name="about"),
	path('AfricanUs/Services', views.services, name="services"),
	path('AfricanUs/Contact', views.contact, name="contact"),


]
