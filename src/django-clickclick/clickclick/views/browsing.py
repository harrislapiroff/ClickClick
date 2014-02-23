from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from clickclick.models import PhotoSet, Photo
from clickclick.views.base import SinglePhotoMixin, SinglePhotoSetMixin


class PhotoSetDetailView(DetailView, SinglePhotoSetMixin):
	"A view for displaying a PhotoSet."
	template_name = 'clickclick/photoset.html'


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
photoset_detail = PhotoSetDetailView.as_view()