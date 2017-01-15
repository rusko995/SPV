from django.contrib import admin
from galerija.models import Album
from galerija.models import Picture

class AlbumAdmin (admin.ModelAdmin):
	list_display = ["title", "pubDate"]
	
	class Meta:
		model = Album
	
class PictureAdmin (admin.ModelAdmin):
	list_display = ["title", "pubDate"]
	
	class Meta:
		model = Picture
	
admin.site.register(Album, AlbumAdmin)
admin.site.register(Picture, PictureAdmin)
