from django.conf.urls import include, url
#from django.contrib.auth import views as auth_views
import frontend

from . import views
from django.contrib.auth.decorators import login_required

app_name = 'backend'
urlpatterns = [
	
	url(r'^backend/$', views.backend_home, name='backend_home'),
	url(r'^backend/operations$', views.OperationsPageView.as_view(), name='operations'),
	url(r'^backend/operations/restaurants$', views.backend_ops_restaurants_PageView.as_view(), name='backend_ops_restaurants'),
	url(r'^backend/operations/attractions$', views.backend_ops_attractions_PageView.as_view(), name='backend_ops_attractions'),
	url(r'^backend/operations/apartments$', views.backend_ops_apartments_PageView.as_view(), name='backend_ops_apartments'),
	url(r'^backend/operations/landing$', views.backend_ops_landing, name='backend_ops_landing'),
	url(r'^backend/operations/about$', views.backend_ops_about, name='backend_ops_about'),

	# url(r'^backend/operations/landing$', views.backend_ops_landing_PageView.as_view(), name='backend_ops_landing'),
	# url(r'^backend/operations/contact$', views.backend_ops_contact_PageView.as_view(), name='backend_ops_contact'),
	# url(r'^backend/operations/about$', views.backend_ops_about_PageView.as_view(), name='backend_ops_about'),
	# url(r'^backend/operations/deals$', views.backend_ops_apartments_PageView.as_view(), name='backend_ops_deals'),


	url(r'^backend/landing/add_restaurant$', views.landing_new_restaurant, name='landing_new_restaurant'),
	url(r'^backend/landing/add_attraction$', views.landing_new_attraction, name='landing_new_attraction'),
	url(r'^backend/landing/add_apartment$', views.landing_new_apartment, name='landing_new_apartment'),

	url(r'^backend/landing/restaurant/(?P<pk>\d+)/$', views.landing_restaurant_detail, name='landing_restaurant_detail'),
	url(r'^backend/landing/attraction/(?P<pk>\d+)/$', views.landing_attraction_detail, name='landing_attraction_detail'),
	url(r'^backend/landing/apartment/(?P<pk>\d+)/$', views.landing_apartment_detail, name='landing_apartment_detail'),

    url(r'^backend/landing/restaurants/(?P<pk>\d+)/edit/$', login_required(views.landing_restaurant_edit), name='landing_restaurant_edit'),
    url(r'^backend/landing/attraction/(?P<pk>\d+)/edit/$', login_required(views.landing_attraction_edit), name='landing_attraction_edit'),
    url(r'^backend/landing/apartment/(?P<pk>\d+)/edit/$', login_required(views.landing_apartment_edit), name='landing_apartment_edit'),

	url(r'^backend/landing/restaurants/(?P<pk>\d+)/remove/$', login_required(views.landing_restaurant_remove), name='landing_restaurant_remove'),
	url(r'^backend/landing/attraction/(?P<pk>\d+)/remove/$', login_required(views.landing_attraction_remove), name='landing_attraction_remove'),
	url(r'^backend/landing/apartment/(?P<pk>\d+)/remove/$', login_required(views.landing_apartment_remove), name='landing_apartment_remove'),


	url(r'^backend/about/add_page_title$', views.about_new_pageTitle, name='about_new_pageTitle'),
	url(r'^backend/about/add_presentation$', views.about_new_presentation, name='about_new_presentation'),
	url(r'^backend/about/add_team_title$', views.about_new_teamTitle, name='about_new_teamTitle'),
	url(r'^backend/about/add_member1$', views.about_new_member1, name='about_new_member1'),
	url(r'^backend/about/add_member2$', views.about_new_member2, name='about_new_member2'),
	url(r'^backend/about/add_member3$', views.about_new_member3, name='about_new_member3'),

	url(r'^backend/about/page_title/(?P<pk>\d+)/$', views.about_pageTitle_detail, name='about_pageTitle_detail'),
	url(r'^backend/about/presentation/(?P<pk>\d+)/$', views.about_presentation_detail, name='about_presentation_detail'),
	url(r'^backend/about/team_title/(?P<pk>\d+)/$', views.about_teamTitle_detail, name='about_teamTitle_detail'),
	url(r'^backend/about/member1/(?P<pk>\d+)/$', views.about_member1_detail, name='about_memberOne_detail'),
	url(r'^backend/about/member2/(?P<pk>\d+)/$', views.about_member2_detail, name='about_memberTwo_detail'),
	url(r'^backend/about/member3/(?P<pk>\d+)/$', views.about_member3_detail, name='about_memberThree_detail'),

	url(r'^backend/about/title/(?P<pk>\d+)/edit/$', login_required(views.about_pageTitle_edit), name='about_title_edit'),
	url(r'^backend/about/presentation/(?P<pk>\d+)/edit/$', login_required(views.about_presentation_edit), name='about_presentation_edit'),
	url(r'^backend/about/team/(?P<pk>\d+)/edit/$', login_required(views.about_teamTitle_edit), name='about_teamTitle_edit'),
	url(r'^backend/about/member1/(?P<pk>\d+)/edit/$', login_required(views.about_member1_edit), name='about_member1_edit'),
	url(r'^backend/about/member2/(?P<pk>\d+)/edit/$', login_required(views.about_member2_edit), name='about_member2_edit'),
	url(r'^backend/about/member3/(?P<pk>\d+)/edit/$', login_required(views.about_member3_edit), name='about_member3_edit'),

	url(r'^backend/about/title/(?P<pk>\d+)/remove/$', login_required(views.about_pageTitle_remove), name='about_title_remove'),
	url(r'^backend/about/presentation/(?P<pk>\d+)/remove/$', login_required(views.about_presentation_remove), name='about_presentation_remove'),
	url(r'^backend/about/team/(?P<pk>\d+)/remove/$', login_required(views.about_teamTitle_remove), name='about_teamTitle_remove'),
	url(r'^backend/about/member1/(?P<pk>\d+)/remove/$', login_required(views.about_member1_remove), name='about_member1_remove'),
	url(r'^backend/about/member2/(?P<pk>\d+)/remove/$', login_required(views.about_member2_remove), name='about_member2_remove'),
	url(r'^backend/about/member3/(?P<pk>\d+)/remove/$', login_required(views.about_member3_remove), name='about_member3_remove'),


	url(r'^backend/staff/list/$', login_required(views.staff_list), name='staff_list'),


    url(r'^signup/$', views.signup, name='signup'),
]

