from django.conf.urls import include, url
#from django.contrib.auth import views as auth_views
import backend
from . import views
from django.contrib.auth.decorators import login_required

app_name='frontend'
urlpatterns = [

	url(r'^$', views.frontend_home, name='frontend_home'),
	#url(r'^about$', views.AboutPageView.as_view(), name='AboutPageView'),
	url(r'^about$', views.frontend_contact, name='frontend_contact'),
]