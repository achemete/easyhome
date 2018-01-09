# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect, render, get_object_or_404

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.views.generic import TemplateView 

from backend.models import *

import backend
####
## frontend Views
####

def frontend_home(request):
	restaurants = Restaurants.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	attractions = Attractions.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	apartments = Apartments.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'frontend/home.html', {'restaurants': restaurants, 'attractions': attractions, 'apartments':apartments})

def frontend_contact(request):
	pageTitles = About_PageTitle.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	#attractions = Attractions.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	#apartments = Apartments.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'frontend/about.html', {'pageTitles': pageTitles})#, 'attractions': attractions, 'apartments':apartments})

# class AboutPageView(TemplateView):
# 	template_name = "frontend/about.html"