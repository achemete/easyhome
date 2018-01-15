# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

#from ckeditor_uploader.fields import RichTextUploadingField
#from ckeditor.fields import RichTextField

class Attractions(models.Model):
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	#text = RichTextUploadingField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

class Restaurants(models.Model):
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	#text = RichTextUploadingField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

class Apartments(models.Model):
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	#text = RichTextUploadingField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

class About_PageTitle(models.Model):
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

class About_PresentationText(models.Model):
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	#text = RichTextUploadingField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

class About_TeamTitle(models.Model):
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

class About_MemberOne(models.Model):
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	#text = RichTextUploadingField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

class About_MemberTwo(models.Model):
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	#text = RichTextUploadingField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

class About_MemberThree(models.Model):
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	#text = RichTextUploadingField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

# 	def publish(self):
# 		self.published_date = timezone.now()
# 		self.save()

# 	def __unicode__(self):
# 		return self.title
# 	#def __str__(self):
# 	#    return self.title

# class Sectionright(models.Model):
# 	author = models.ForeignKey('auth.User')
# 	title = models.CharField(max_length=200)
# 	text = models.TextField()
# 	#text = RichTextUploadingField()
# 	created_date = models.DateTimeField(
# 			default=timezone.now)
# 	published_date = models.DateTimeField(
# 			blank=True, null=True)

# 	def publish(self):
# 		self.published_date = timezone.now()
# 		self.save()

# 	def __unicode__(self):
# 		return self.title

# class Algoleft(models.Model):
# 	author = models.ForeignKey('auth.User')
# 	title = models.CharField(max_length=200)
# 	text = models.TextField()
# 	#text = RichTextUploadingField()
# 	created_date = models.DateTimeField(
# 			default=timezone.now)
# 	published_date = models.DateTimeField(
# 			blank=True, null=True)

# 	def publish(self):
# 		self.published_date = timezone.now()
# 		self.save()

# 	def __unicode__(self):
# 		return self.title

# class Algoright(models.Model):
# 	author = models.ForeignKey('auth.User')
# 	title = models.CharField(max_length=200)
# 	text = models.TextField()
# 	#text = RichTextUploadingField()
# 	created_date = models.DateTimeField(
# 			default=timezone.now)
# 	published_date = models.DateTimeField(
# 			blank=True, null=True)

# 	def publish(self):
# 		self.published_date = timezone.now()
# 		self.save()

# 	def __unicode__(self):
# 		return self.title
