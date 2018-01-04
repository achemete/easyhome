from django.conf.urls import include, url
#from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [

	url(r'^backend/$', views.backend_home, name='backend'),

]