from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.views.generic.detail import SingleObjectMixin

from clickclick.models import PhotoSet, Photo


class SinglePhotoMixin(SingleObjectMixin):
	"""
	Provides the ability to retrieve a single photo.
	"""
	
	model = Photo
	context_object_name = 'photo'
	
	def get_object(self, queryset=None):
		"""
		Returns the object the view is displaying.
		
		Requires `username`, `photo_slug`, and `photoset_slug` argument in the URLconf.
		"""
		# Use a custom queryset if provided.
		if queryset is None:
			queryset = self.get_queryset()
		# Extract slugs.
		username = self.kwargs.get('username')
		photoset_slug = self.kwargs.get('photoset_slug')
		photo_slug = self.kwargs.get('photo_slug')
		# If one of these is missing, it is an error.
		if not (username and photoset_slug and photo_slug):
			raise AttributeError(u"View %s must be called with a username, photoset_slug, and photo_slug." % self.__class__.__name__)
		try:
			obj = queryset.get(photoset__owner__username__exact=self.kwargs['username'], slug__exact=self.kwargs['photo_slug'], photoset__slug__exact=self.kwargs['photoset_slug'])
		except ObjectDoesNotExist:
			raise Http404(u"No Photos found matching the query")
		return obj

class SinglePhotoSetMixin(SingleObjectMixin):
	"""
	Provides the ability to retrieve a single photoset.
	"""
	
	model = PhotoSet
	context_object_name = 'photoset'
	
	def get_object(self, queryset=None):
		"""
		Returns the object the view is displaying.
		
		Requires a `photoset_slug` argument in the URLconf.
		"""
		if queryset is None:
			queryset = self.get_queryset()
		try:
			object = queryset.get(slug=self.kwargs['photoset_slug'])
		except ObjectDoesNotExist:
			raise Http404(u"No Photoset found matching the query")
		return object

class PhotoPermissionMixin(SingleObjectMixin):
	"""
	Checks for permissions on a photo before either dispatching the view or returning HttpReponseForbidden.
	"""
	
	def dispatch(self, request, photoset_slug=None, photo_slug=None, *args, **kwargs):
		"Check if the current user has permission to edit this photoset. If not, return forbidden."
		# if no photoset is specified, return forbidden
		if photoset_slug == None or photo_slug == None:
			return HttpResponseForbidden('No photo specified.')
		# grab the photoset and photo from database
		self.photoset = get_object_or_404(PhotoSet, slug=photoset_slug)
		self.photo = get_object_or_404(Photo, slug=photo_slug, photoset=self.photoset)
		# if they do not own the photoset, return forbidden
		if self.photo.owner != request.user:
			return HttpResponseForbidden('Forbidden. You do not own that photo.')
		# otherwise, continue as usual
		return super(PhotoPermissionMixin, self).dispatch(request, photoset_slug=photoset_slug, photo_slug=photo_slug, *args, **kwargs)
	

class PhotoSetPermissionMixin(SingleObjectMixin):
	"""
	Checks for permissions on a photoset before either dispatching the view or returning HttpResponseForbidden.
	"""
	
	def dispatch(self, request, photoset_slug=None, *args, **kwargs):
		"""
		Check if the current user has permission to edit this photoset. If not, return forbidden.
		"""
		# if no photoset is specified, return forbidden
		if photoset_slug == None:
			return HttpResponseForbidden('No photoset specified.')
		# grab the photoset from database
		self.photoset = get_object_or_404(PhotoSet, slug=photoset_slug)
		# if they do not own the photoset, return forbidden
		if self.photoset.owner != request.user:
			return HttpResponseForbidden('Forbidden. You do not own that photoset.')
		# otherwise, continue as usual
		return super(PhotoSetPermissionMixin, self).dispatch(request, photoset_slug=photoset_slug, *args, **kwargs)