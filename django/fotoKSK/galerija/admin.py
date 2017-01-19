from django.contrib import admin
from galerija.models import Album
from galerija.models import Picture

class AlbumAdmin (admin.ModelAdmin):
	"""How albums are presented on admin site"""
	list_display = ["title", "author", "pubDate"]
	
	class Meta:
		model = Album
	
class PictureAdmin (admin.ModelAdmin):
	"""How pictures are presented on admin site"""
	list_display = ["title", "author"]
	
	class Meta:
		model = Picture
	
admin.site.register(Album, AlbumAdmin)
admin.site.register(Picture, PictureAdmin)
