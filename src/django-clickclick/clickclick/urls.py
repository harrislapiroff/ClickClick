from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from clickclick.utils import reverse_lazy

urlpatterns = patterns('',
	url(r'^$', RedirectView.as_view(url=reverse_lazy('clickclick.photoset_list')), name="clickclick.home"),
	# photo/set creation and updating
	url(r'^create/$', 'clickclick.views.create_photoset', name='clickclick.create_photoset'),
	url(r'^delete/(?P<photoset_slug>[\w-]+)/$', 'clickclick.views.delete_photoset', name='clickclick.delete_photoset'),
	url(r'^edit/(?P<photoset_slug>[\w-]+)/$', 'clickclick.views.edit_photoset', name='clickclick.edit_photoset'),
	url(r'^(?P<photoset_slug>[\w-]+)/create/$', 'clickclick.views.add_photo', name='clickclick.add_photo'),
	url(r'^(?P<photoset_slug>[\w-]+)/delete/(?P<photo_slug>[-\w]+)/$', 'clickclick.views.delete_photo', name='clickclick.delete_photo'),
	url(r'^(?P<photoset_slug>[\w-]+)/edit/(?P<photo_slug>[-\w]+)/$', 'clickclick.views.edit_photo', name='clickclick.edit_photo'),
	# photo/set management
	url(r'^photosets/$', 'clickclick.views.photoset_list', name='clickclick.photoset_list'),
	# photo/set browsing
	url(r'^(?P<photoset_slug>[\w-]+)/$', 'clickclick.views.photoset_detail', name='clickclick.photoset'),
	url(r'^(?P<photoset_slug>[\w-]+)/(?P<photo_slug>[-\w]+)/$', 'clickclick.views.photo_detail', name='clickclick.photo'),
)