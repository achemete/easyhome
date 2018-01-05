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

from backend.models import *

####
## frontend Views
####

def frontend_home(request):
	sections = Restaurants.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	#sectionsR = Sectionright.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'frontend/home.html', {'sections': sections})#, 'sectionsR': sectionsR})