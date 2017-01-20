from django import forms
from django.utils.translation import ugettext_lazy as _

'''
class SearchForm(forms.Form):
	"""
	The SearchForm\n
	It is used for finding a secific gallery
	"""
	search = forms.CharField(label = "",max_length=64,widget=forms.TextInput(attrs={'placeholder': _('Vnesite iskalni niz..'),'type':'search'}))
	'''
	
class ContactForm(forms.Form):
	"""Contact form on index site"""
	contact_name = forms.CharField(required=True, max_length=50)
	contact_email = forms.EmailField(required=True)
	content = forms.CharField(required=True, widget=forms.Textarea)

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['contact_name'].label = _("Your name:")
		self.fields['contact_email'].label = _("Your email:")
		self.fields['content'].label = _("What do you want to say?")
