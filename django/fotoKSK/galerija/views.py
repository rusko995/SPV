from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Picture

# Create your views here.
def index(request):
	queryset = Album.objects.all()
	context = {
		"albums": queryset,
	}
	#slike=[]
	#for item in queryset:
	#	slike.append(item.get_cover_photo())
	#context['slike']=slike
	
	return render (request, 'galerija/home.html', context)
	

#def picture_view(request,album_id)