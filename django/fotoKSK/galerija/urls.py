from django.conf.urls import url

#pika pomeni, da importamo iz trenutnega packega
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^contact/$', views.contact, name='contact'),
    url(r'^', views.index, name='index'),
	#url(r'^search/$', views.search, name='search'),
	#url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post, template_name = 'blog/post.html')),
]