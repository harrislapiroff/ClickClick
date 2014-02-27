from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

from clickclick.models import PhotoSet, Photo
from clickclick.forms import PhotoSetForm, PhotoCreateForm
from clickclick.views.base import SinglePhotoMixin, SinglePhotoSetMixin, PhotoPermissionMixin, PhotoSetPermissionMixin


class PhotoSetCreateView(CreateView):
	"A view for creating photosets."
	model = PhotoSet
	template_name = "clickclick/form.html"
	form_class = PhotoSetForm
	
	def get_form_kwargs(self):
		kwargs = super(PhotoSetCreateView, self).get_form_kwargs()
		instance = self.model(owner=self.request.user)
		kwargs.update(instance=instance)
		return kwargs
	
	def get_form_class(self):
		return self.form_class


class PhotoCreateView(CreateView):
	"A view for creating photos within photosets. Method `dispatch` must be passed a photoset_slug kwarg."
	
	model = Photo
	template_name = "clickclick/form.html"
	form_class = PhotoCreateForm
	
	def dispatch(self, request, photoset_slug=None, *args, **kwargs):
		# if no photoset is specified, return forbidden
		if photoset_slug == None:
			return HttpResponseForbidden('No photoset specified.')
		# grab the photoset from database
		self.photoset = get_object_or_404(PhotoSet, slug=photoset_slug)
		# if they do not own the photoset, return forbidden
		if self.photoset.owner != request.user:
			return HttpResponseForbidden('Forbidden. You do not own that photoset.')
		# otherwise, continue as usual
		return super(PhotoCreateView, self).dispatch(request, *args, **kwargs)
	
	def get_form_kwargs(self):
		kwargs = super(PhotoCreateView, self).get_form_kwargs()
		instance = self.model(owner=self.request.user, photoset=self.photoset)
		kwargs.update(instance=instance)
		return kwargs
	
	def get_form_class(self):
		return self.form_class


class PhotoSetListView(ListView):
	"A view for listing all the photosets owned by the current user."
	model = PhotoSet
	paginate_by = 10
	context_object_name = 'photosets'
	template_name = "clickclick/photoset_list.html"
	
	def get_queryset(self):
		return PhotoSet.objects.filter(owner=self.request.user)


class PhotoUpdateView(UpdateView, PhotoPermissionMixin):
	"A view for editing photos."
	template_name = "clickclick/form.html"
	form_class = PhotoCreateForm


class PhotoSetUpdateView(UpdateView, PhotoSetPermissionMixin):
	"A view for editing PhotoSets."
	template_name = "clickclick/form.html"
	form_class = PhotoSetForm

class PhotoSetDeleteView(DeleteView, PhotoSetPermissionMixin):
	"A view for deleting PhotoSets."
	template_name = "clickclick/photoset_delete_confirm.html"
	
	@property
	def success_url(self):
		return reverse('clickclick.views.photoset_list')


class PhotoDeleteView(DeleteView, PhotoPermissionMixin):
	"A view for deleting Photos."
	model = Photo
	template_name = "clickclick/photo_delete_confirm.html"
	context_object_name = 'photo'
	
	@property
	def success_url(self):
		return reverse('clickclick.views.photoset_detail', args=(self.kwargs['photoset_slug'],))


create_photoset = login_required(PhotoSetCreateView.as_view())
edit_photoset = login_required(PhotoSetUpdateView.as_view())
delete_photoset = login_required(PhotoSetDeleteView.as_view())
add_photo = login_required(PhotoCreateView.as_view())
edit_photo = login_required(PhotoUpdateView.as_view())
delete_photo = login_required(PhotoDeleteView.as_view())
photoset_list = login_required(PhotoSetListView.as_view())