from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from PIL import Image
# Create your models here.

class Album(models.Model):
	title = models.CharField(max_length=100, default='')
	pubDate = models.DateTimeField( default=timezone.now )
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	naslovnaSlika = models.ImageField()
	def __str__(self):
		return self.title
		
	def was_published_recently(self):
		return self.pubDate >= timezone.now() - timezone.timedelta(days=1)
	
			
	class Meta:
		ordering=["-pubDate"]

class Picture(models.Model):
	title = models.CharField(max_length=100, default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	pubDate = models.DateTimeField( default=timezone.now )
	image = models.ImageField(null=False)
	album = models.ForeignKey(Album)
	
	def __unicode__(self):
		return self.title
	
	def get_image_filename(self):
		return self.title
	
	class Meta:
		ordering=["-pubDate"]
	
	

	