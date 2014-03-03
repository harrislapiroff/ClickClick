from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from clickclick.forms.fields import MultiFileField
from clickclick.models import PhotoSet, Photo

__all__ = ('PhotoSetForm', 'PhotoUpdateForm', 'PhotoUploadForm',)

class PhotoSetForm(forms.ModelForm):
	slug = forms.CharField(max_length=50, label="URL", widget=forms.TextInput(attrs={'data-prepopulate-slug':'id_title'}))
	
	def __init__(self, *args, **kwargs):
		super(PhotoSetForm, self).__init__(*args, **kwargs)
		url = "http://%s%s" % ("localhost", reverse('clickclick.photoset', args=(self.instance.owner.username, '--INPUT_HERE--',)))
		self.fields['slug'].widget.attrs.update({'data-slug-url': url})
	
	class Meta:
		model = PhotoSet
		exclude = ('owner',)


class PhotoUpdateForm(forms.ModelForm):
	slug = forms.CharField(max_length=50, label="URL", widget=forms.TextInput(attrs={'data-prepopulate-slug':'id_title'}))
	
	def __init__(self, *args, **kwargs):
		super(PhotoUpdateForm, self).__init__(*args, **kwargs)
		url = "http://%s%s" % ("localhost", reverse('clickclick.photo', args=(self.instance.photoset.owner.username, self.instance.photoset.slug, '--INPUT_HERE--',)))
		self.fields['slug'].widget.attrs.update({'data-slug-url': url})
		
	class Meta:
		model = Photo
		exclude = ('owner', 'photoset', 'image')


class UserUpdateForm(UserChangeForm):
	class Meta:
		fields = ('first_name', 'last_name', 'username', 'email')
		model = User


class PhotoUploadForm(forms.Form):
	images = MultiFileField()
