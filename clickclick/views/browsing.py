from django.contrib.auth.models import User
from django.http import Http404
from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext

from clickclick.forms import PhotoUploadForm
from clickclick.models import PhotoSet, Photo
from clickclick.views.base import SinglePhotoMixin, SinglePhotoSetMixin


def photoset_detail(request, username, photoset_slug):
	photoset = get_object_or_404(PhotoSet, owner__username=username, slug=photoset_slug)

	# If privacy settings do not allow this photoset to be publicly browsed, short-circuit.
	if photoset.privacy == PhotoSet.PRIVATE and request.user != photoset.owner:
		raise Http404("PhotoSet not found.")

	kwargs = {'photoset': photoset}

	if request.user == photoset.owner:
		kwargs['photo_form'] = PhotoUploadForm(initial={'photoset': photoset.pk})
	
	return render(request, 'clickclick/photoset.html', kwargs)


def photo_detail(request, username, photoset_slug, photo_slug):
	photoset = get_object_or_404(PhotoSet, owner__username=username, slug=photoset_slug)
	photo = get_object_or_404(Photo, photoset=photoset, slug=photo_slug)

	# If privacy settings do not allow this photoset to be publicly browsed, short-circuit.
	if photoset.privacy == PhotoSet.PRIVATE and request.user != photoset.owner:
		raise Http404("Photo not found.")

	return render(request, 'clickclick/photo.html', {'photoset': photoset, 'photo': photo})


def user_photoset_list(request, username):
	user = get_object_or_404(User, username=username)
	photosets = PhotoSet.objects.filter(owner=user)
	return render(request, 'clickclick/photoset_list.html', {'owner': user, 'photosets': photosets})
