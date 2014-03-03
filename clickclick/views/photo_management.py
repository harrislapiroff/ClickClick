from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseForbidden, HttpResponseNotAllowed
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
		return reverse('clickclick.views.user_photoset_list', kwargs={'username': self.request.user.username})


class PhotoDeleteView(DeleteView, PhotoPermissionMixin):
	"A view for deleting Photos."
	model = Photo
	template_name = "clickclick/photo_delete_confirm.html"
	context_object_name = 'photo'
	
	@property
	def success_url(self):
		return reverse('clickclick.views.photoset_detail', args=(self.request.user.username, self.kwargs['photoset_slug'],))


def upload_photos(request, photoset_slug):
	if request.POST:
		photoset = get_object_or_404(PhotoSet, slug=photoset_slug)

		if photoset.owner != request.user:
			# If the user does not own this photoset, short-circuit.
			return HttpResponseForbidden("You do not have permission to upload files to &ldquo;%s&rdquo;" % photoset.title)
		
		# Otherwise, iterate over the file list, creating Image objects.
		file_list = request.FILES.getlist('images')
		for _file in file_list:
			# TODO: convert this for loop to a bulk create
			# TODO: better slug generation--this leaves the potential for unresolved uniqueness conflicts, since photoset and slug must be unique
			Photo.objects.create(title=_file.name, image=_file, owner=request.user, photoset=photoset)
		return redirect(photoset)
	# Only POST is allowed.
	return HttpResponseNotAllowed(("POST",))

create_photoset = login_required(PhotoSetCreateView.as_view())
edit_photoset = login_required(PhotoSetUpdateView.as_view())
delete_photoset = login_required(PhotoSetDeleteView.as_view())
edit_photo = login_required(PhotoUpdateView.as_view())
delete_photo = login_required(PhotoDeleteView.as_view())
photoset_list = login_required(PhotoSetListView.as_view())
