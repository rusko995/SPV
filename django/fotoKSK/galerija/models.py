from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from PIL import Image
# Create your models here.

class Album(models.Model):
	"""Album in gallery"""
	title = models.CharField(max_length=100, default='')
	pubDate = models.DateTimeField( default=timezone.now )
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	naslovnaSlika = models.ImageField()
	def __str__(self):
		"""Returns Album's title"""
		return self.title
		
	def was_published_recently(self):
		"""Returns True, if the article is recent (i.e. recent than 5 days)"""
		return self.pubDate >= timezone.now() - timezone.timedelta(days=5)
		
	def has_cover_photo(self):
		"""Returns True if Album has cover photo"""
		return bool(self.naslovnaSlika)
	
			
	class Meta:
		ordering=["-pubDate"]

class Picture(models.Model):
	"""Picture in album"""
	title = models.CharField(max_length=100, default='')
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	pubDate = models.DateTimeField( default=timezone.now )
	image = models.ImageField(null=False)
	album = models.ForeignKey(Album)
	
	def get_image_filename(self):
		"""returns image filename"""
		return self.title
	
	class Meta:
		ordering=["-pubDate"]
	
	

	