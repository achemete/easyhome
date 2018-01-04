# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

#from ckeditor_uploader.fields import RichTextUploadingField
#from ckeditor.fields import RichTextField

# class Section(models.Model):
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



