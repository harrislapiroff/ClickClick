from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from clickclick.models import PhotoSet, Photo

__all__ = ('PhotoSetForm', 'PhotoCreateForm',)

class PhotoSetForm(forms.ModelForm):
	slug = forms.CharField(max_length=50, label="URL", widget=forms.TextInput(attrs={'data-prepopulate-slug':'id_title'}))
	
	def __init__(self, *args, **kwargs):
		super(PhotoSetForm, self).__init__(*args, **kwargs)
		url = "http://%s%s" % ("localhost", reverse('clickclick.photoset', args=('--INPUT_HERE--',)))
		self.fields['slug'].widget.attrs.update({'data-slug-url': url})
	
	class Meta:
		model = PhotoSet
		exclude = ('owner',)


class PhotoCreateForm(forms.ModelForm):
	slug = forms.CharField(max_length=50, label="URL", widget=forms.TextInput(attrs={'data-prepopulate-slug':'id_title'}))
	
	def __init__(self, *args, **kwargs):
		super(PhotoCreateForm, self).__init__(*args, **kwargs)
		url = "http://%s%s" % ("localhost", reverse('clickclick.photo', args=(self.instance.photoset.slug, '--INPUT_HERE--',)))
		self.fields['slug'].widget.attrs.update({'data-slug-url': url})
		
	class Meta:
		model = Photo
		exclude = ('owner', 'photoset', 'index')

class UserUpdateForm(UserChangeForm):
	class Meta:
		fields = ('first_name', 'last_name', 'username', 'email')
		model = User

class FastPhotoCreateForm(forms.ModelForm):
	class Meta:
		model = Photo
		fields = ('image',)