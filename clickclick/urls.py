from django.conf.urls import patterns, include, url

from clickclick.utils import reverse_lazy
from clickclick.moderators import PhotoModerator # Need to ensure comment moderators get loaded.

urlpatterns = patterns('',
	url(r'^$', 'clickclick.views.home', name="clickclick.home"),

	# photo/set creation and updating
	url(r'^create/$', 'clickclick.views.create_photoset', name='clickclick.create_photoset'),
	url(r'^delete/(?P<photoset_slug>[\w-]+)/$', 'clickclick.views.delete_photoset', name='clickclick.delete_photoset'),
	url(r'^edit/(?P<photoset_slug>[\w-]+)/$', 'clickclick.views.edit_photoset', name='clickclick.edit_photoset'),
	url(r'^photo_upload/(?P<photoset_slug>[\w-]+)/', 'clickclick.views.upload_photos', name='clickclick.upload_photos'),
	url(r'^photo_delete/(?P<photoset_slug>[\w-]+)/(?P<photo_slug>[-\w]+)/$', 'clickclick.views.delete_photo', name='clickclick.delete_photo'),
	url(r'^photo_edit/(?P<photoset_slug>[\w-]+)/(?P<photo_slug>[-\w]+)/$', 'clickclick.views.edit_photo', name='clickclick.edit_photo'),

	# comments
	url(r'^approve_comment/(?P<comment_id>[0-9]+)/', 'clickclick.views.approve_photo_comment', name="clickclick.approve_comment"),
	url(r'^remove_comment/(?P<comment_id>[0-9]+)/', 'clickclick.views.remove_photo_comment', name="clickclick.remove_comment"),

	# photo/set browsing
	url(r'^(?P<username>[\w-]+)/$', 'clickclick.views.user_photoset_list', name='clickclick.user_photoset_list'),
	url(r'^(?P<username>[\w-]+)/(?P<photoset_slug>[\w-]+)/$', 'clickclick.views.photoset_detail', name='clickclick.photoset'),
	url(r'^(?P<username>[\w-]+)/(?P<photoset_slug>[\w-]+)/(?P<photo_slug>[-\w]+)/$', 'clickclick.views.photo_detail', name='clickclick.photo'),
)