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

import frontend

from .models import Attractions, Restaurants, Apartments
from .forms import PostRestaurant, PostAttraction, PostApartment

####
## Backend Views
####

class OperationsPageView(TemplateView):
	template_name = "backend/operations.html"

def backend_home(request):
	return render(request, 'backend/back_end_home.html')

def backend_new_restaurant(request):
	if request.method == "POST":
		form = PostRestaurant(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:backend_restaurant_detail', pk=section.pk)
	else:
		form = PostRestaurant()
	return render(request, 'backend/backend_restaurant_new.html', {'form': form})

def backend_new_attraction(request):
	if request.method == "POST":
		form = PostAttraction(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:backend_attraction_detail', pk=section.pk)
	else:
		form = PostAttraction()
	return render(request, 'backend/backend_attraction_new.html', {'form': form})

def backend_new_apartment(request):
	if request.method == "POST":
		form = PostApartment(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:backend_apartment_detail', pk=section.pk) ### add app backend
	else:
		form = PostApartment()
	return render(request, 'backend/backend_apartment_new.html', {'form': form})

def backend_restaurant_detail(request, pk):
	section = get_object_or_404(Restaurants, pk=pk)
	return render(request, 'backend/backend_restaurant_detail.html', {'section': section})

def backend_attraction_detail(request, pk):
	section = get_object_or_404(Attractions, pk=pk)
	return render(request, 'backend/backend_attraction_detail.html', {'section': section})

def backend_apartment_detail(request, pk):
	section = get_object_or_404(Apartments, pk=pk)
	return render(request, 'backend/backend_apartment_detail.html', {'section': section})

def backend_restaurant_edit(request, pk):
	section = get_object_or_404(Restaurants, pk=pk)
	if request.method == "POST":
		form = PostRestaurant(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:backend_restaurant_detail', pk=section.pk)
	else:
		form = PostRestaurant(instance=section)
	return render(request, 'backend/section_edit.html', {'form': form})

def backend_attraction_edit(request, pk):
	section = get_object_or_404(Attractions, pk=pk)
	if request.method == "POST":
		form = PostAttraction(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:backend_attraction_detail', pk=section.pk)
	else:
		form = PostAttraction(instance=section)
	return render(request, 'backend/section_edit.html', {'form': form})

def backend_apartment_edit(request, pk):
	section = get_object_or_404(Apartments, pk=pk)
	if request.method == "POST":
		form = PostApartment(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:backend_apartment_detail', pk=section.pk)
	else:
		form = PostApartment(instance=section)
	return render(request, 'backend/section_edit.html', {'form': form})