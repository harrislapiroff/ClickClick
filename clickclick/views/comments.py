import django_comments

from django.conf import settings
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404

from django_comments.models import Comment
from django_comments.views.moderation import perform_approve, perform_delete


def approve_photo_comment(request, comment_id, next=None):
	"""
	Approve a comment on a photo (i.e., mark it as public). This view also
	checks the current user has ownership of the photoset that the comment
	belongs to.

	Redirects to provided next arg or to the photo's page upon approval.

	"""

	comment = get_object_or_404(django_comments.get_model(), pk=comment_id, site__pk=settings.SITE_ID)

	try:
		photo = comment.content_object
		photoset = photo.photoset
	except AttributeError:
		raise

	if request.user != photoset.owner:
		raise PermissionDenied

	perform_approve(request, comment)

	messages.add_message(request, messages.SUCCESS, "Comment approved.")

	return redirect(photo if not next else next)


def remove_photo_comment(request, comment_id, next=None):

	comment = get_object_or_404(django_comments.get_model(), pk=comment_id, site__pk=settings.SITE_ID)

	try:
		photo = comment.content_object
		photoset = photo.photoset
	except AttributeError:
		raise

	if request.user != photoset.owner:
		raise PermissionDenied

	perform_delete(request, comment)

	messages.add_message(request, messages.SUCCESS, "Comment removed.")

	return redirect(photo if not next else next)