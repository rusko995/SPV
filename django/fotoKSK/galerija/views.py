from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Picture
from .forms import ContactForm

from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template

#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
	"""The index page
  
	This is the index of the app. It contains galleries from KSK photographers.
	It has contact form and search bar.
	
	Keyword arguments:
	request -- the django requst object
	"""
	queryset = Album.objects.all()
	context = {
		"albums": queryset,
	}
	#slike=[]
	#for item in queryset:
	#	slike.append(item.get_cover_photo())
	#context['slike']=slike
	
	return render (request, 'galerija/home.html', context)
	
	
def contact(request):
	"""The contact page
  
	This is the contact page through which you can contact developer of this website.
	
	Keyword arguments:
	request -- the django requst object
	"""
	form_class = ContactForm()

	# new logic!
	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get( 'contact_name', '')
			contact_email = request.POST.get('contact_email', '')
			form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
			template = get_template('contact_template.txt')
			context = Context({'contact_name': contact_name, 'contact_email': contact_email, 'form_content': form_content, })
			content = template.render(context)
			email = EmailMessage("New contact form submission", content, "Your website" +'', ['youremail@gmail.com'], headers = {'Reply-To': contact_email })
			email.send()
			return redirect('contact')

	return render(request, 'galerija/contact.html', {'form': form_class,})
	
def gallery_view(request, album_id):
	album=Album.objects.get(id=album_id)
	queryset = Picture.objects.filter(album=album)
	context = {
		"pictures": queryset,
	}
	return render(request, 'galerija/gallery.html', context)
