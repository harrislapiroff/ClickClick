from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext

from clickclick.forms import PhotoUploadForm
from clickclick.models import PhotoSet, Photo
from clickclick.views.base import SinglePhotoMixin, SinglePhotoSetMixin


def photoset_detail(request, photoset_slug):
	photoset = get_object_or_404(PhotoSet, slug=photoset_slug)
	kwargs = {'photoset': photoset}

	if request.user == photoset.owner:
		kwargs['photo_form'] = PhotoUploadForm(initial={'photoset': photoset.pk})
	
	return render(request, 'clickclick/photoset.html', kwargs)


class PhotoSetView(ListView):
	"A view for displaying a PhotoSet as a ListView subclass instead of a detail view. Not currently complete or used."
	model = Photo
	template_name = 'clickclick/photoset.html'
	context_object_name = 'photos'
	paginate_by = 50


class PhotoDetailView(DetailView, SinglePhotoMixin):
	"A view for displaying a single Photo."
	template_name = 'clickclick/photo.html'

photo_detail = PhotoDetailView.as_view()
