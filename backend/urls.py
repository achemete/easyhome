from django.conf.urls import include, url
#from django.contrib.auth import views as auth_views
import frontend
from . import views

from django.contrib.auth.decorators import login_required

app_name = 'backend'
urlpatterns = [
	url(r'^backend/$', views.backend_home, name='backend_home'),
	url(r'^backend/operations$', views.OperationsPageView.as_view(), name='operations'), 
	url(r'^backend/add_restaurant$', views.backend_new_restaurant, name='backend_new_restaurant'),
	url(r'^backend/add_attraction$', views.backend_new_attraction, name='backend_new_attraction'),
	url(r'^backend/add_apartment$', views.backend_new_apartment, name='backend_new_apartment'),

	url(r'^backend/content/restaurant/(?P<pk>\d+)/$', views.backend_restaurant_detail, name='backend_restaurant_detail'),
	url(r'^backend/content/attraction/(?P<pk>\d+)/$', views.backend_attraction_detail, name='backend_attraction_detail'),
	url(r'^backend/content/apartment/(?P<pk>\d+)/$', views.backend_apartment_detail, name='backend_apartment_detail'),

    url(r'^backend/content/restaurants/(?P<pk>\d+)/edit/$', login_required(views.backend_restaurant_edit), name='backend_restaurant_edit'),
    url(r'^backend/content/attraction/(?P<pk>\d+)/edit/$', login_required(views.backend_attraction_edit), name='backend_attraction_edit'),
    url(r'^backend/content/apartment/(?P<pk>\d+)/edit/$', login_required(views.backend_apartment_edit), name='backend_apartment_edit'),

]

