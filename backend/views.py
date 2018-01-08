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

# class backend_ops_landing_PageView(TemplateView):
# 	template_name = "backend/backend_ops_landing.html"

# class backend_ops_contact_PageView(TemplateView):
# 	template_name = "backend/backend_ops_contact.html"

# class backend_ops_about_PageView(TemplateView):
# 	template_name = "backend/backend_ops_about.html"

# class backend_ops_deals_PageView(TemplateView):
# 	template_name = "backend/backend_ops_deals.html"

class backend_ops_restaurants_PageView(TemplateView):
	template_name = "backend/backend_ops_restaurants.html"

class backend_ops_attractions_PageView(TemplateView):
	template_name = "backend/backend_ops_attractions.html"

class backend_ops_apartments_PageView(TemplateView):
	template_name = "backend/backend_ops_apartments.html"

def backend_home(request):
	return render(request, 'backend/back_end_home.html')

def backend_ops_landing(request):
	restaurants = Restaurants.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	attractions = Attractions.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	apartments = Apartments.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'backend/backend_ops_landing.html', {'restaurants': restaurants, 'attractions': attractions, 'apartments':apartments})

def landing_new_restaurant(request):
	if request.method == "POST":
		form = PostRestaurant(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:landing_restaurant_detail', pk=section.pk)
	else:
		form = PostRestaurant()
	return render(request, 'backend/landing_restaurant_new.html', {'form': form})

def landing_new_attraction(request):
	if request.method == "POST":
		form = PostAttraction(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:landing_attraction_detail', pk=section.pk)
	else:
		form = PostAttraction()
	return render(request, 'backend/landing_attraction_new.html', {'form': form})

def landing_new_apartment(request):
	if request.method == "POST":
		form = PostApartment(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:landing_apartment_detail', pk=section.pk) ### add app backend
	else:
		form = PostApartment()
	return render(request, 'backend/landing_apartment_new.html', {'form': form})

def landing_restaurant_detail(request, pk):
	section = get_object_or_404(Restaurants, pk=pk)
	return render(request, 'backend/landing_restaurant_detail.html', {'section': section})

def landing_attraction_detail(request, pk):
	section = get_object_or_404(Attractions, pk=pk)
	return render(request, 'backend/landing_attraction_detail.html', {'section': section})

def landing_apartment_detail(request, pk):
	section = get_object_or_404(Apartments, pk=pk)
	return render(request, 'backend/landing_apartment_detail.html', {'section': section})

def landing_restaurant_edit(request, pk):
	section = get_object_or_404(Restaurants, pk=pk)
	if request.method == "POST":
		form = PostRestaurant(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:landing_restaurant_detail', pk=section.pk)
	else:
		form = PostRestaurant(instance=section)
	return render(request, 'backend/section_edit.html', {'form': form})

def landing_attraction_edit(request, pk):
	section = get_object_or_404(Attractions, pk=pk)
	if request.method == "POST":
		form = PostAttraction(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:landing_attraction_detail', pk=section.pk)
	else:
		form = PostAttraction(instance=section)
	return render(request, 'backend/section_edit.html', {'form': form})

def landing_apartment_edit(request, pk):
	section = get_object_or_404(Apartments, pk=pk)
	if request.method == "POST":
		form = PostApartment(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:landing_apartment_detail', pk=section.pk)
	else:
		form = PostApartment(instance=section)
	return render(request, 'backend/section_edit.html', {'form': form})

def landing_restaurant_remove(request, pk):
	restaurants = get_object_or_404(Restaurants, pk=pk)
	restaurants.delete()
	return redirect('backend:backend_ops_landing')

def landing_attraction_remove(request, pk):
	attractions = get_object_or_404(Attractions, pk=pk)
	attractions.delete()
	return redirect('backend:backend_ops_landing')

def landing_apartment_remove(request, pk):
	apartments = get_object_or_404(Apartments, pk=pk)
	apartments.delete()
	return redirect('backend:backend_ops_landing')