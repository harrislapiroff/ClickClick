from django_comments.moderation import CommentModerator, moderator
from clickclick.models import Photo, PhotoSet

class PhotoModerator(CommentModerator):
	email_notification = False

	def allow(self, comment, content_object, request):
		"Returns True if both the super method is true and comments are enabled on the photoset."
		return (super(PhotoModerator, self).allow(comment, content_object, request) and content_object.photoset.comments_enabled != PhotoSet.COMMENTS_OFF)

	def moderate(self, comment, content_object, request):
		"Returns True if either the super method is True or comments on the photoset are moderated."
		return (super(PhotoModerator, self).moderate(comment, content_object, request) or content_object.photoset.comments_enabled == PhotoSet.COMMENTS_MODERATED)


moderator.register(Photo, PhotoModerator)