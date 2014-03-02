from autoslug import AutoSlugField

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class PhotoSet(models.Model):
	"""A photoset with photos in it."""

	PRIVATE = "PR"
	UNLISTED = "UN"
	PUBLIC = "PL"
	PRIVACY_CHOICES = (
		(PRIVATE, "Private"),
		(UNLISTED, "Unlisted"),
		(PUBLIC, "Public"),
	)

	title = models.CharField(max_length=100)
	slug = AutoSlugField(max_length=50, populate_from='title', editable=True, unique_with='owner')
	description = models.TextField(blank=True)
	privacy = models.CharField(max_length=2, choices=PRIVACY_CHOICES, default=PRIVATE)
	owner = models.ForeignKey(User, null=True, related_name='photosets')
	creation_time = models.DateTimeField(auto_now_add=True)
	last_updated_time = models.DateTimeField(auto_now=True)
	
	def get_absolute_url(self):
		return reverse('clickclick.photoset', args=[self.owner.username, self.slug])
	
	def __unicode__(self):
		return self.title

	class Meta:
		unique_together = ('owner', 'slug',)


class Photo(models.Model):
	"""A photo with metadata, which ideally belongs to a photoset. However, it is possible for a photo not to belong to a photoset, and therefore the owner property is necessary."""
	title = models.CharField(max_length=128, blank=True)
	photoset = models.ForeignKey(PhotoSet, related_name='photos')
	slug = AutoSlugField(max_length=128, populate_from='title', editable=True, unique_with='photoset')
	owner = models.ForeignKey(User, null=True, related_name="photos")
	image = models.ImageField(upload_to='photos')
	caption = models.TextField(blank=True)
	upload_time = models.DateTimeField(auto_now_add=True)
	last_updated_time = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		"If the object is new, we're gonna override the save method to reorder the photoset so the new object comes first."
		is_new = self.pk is None
		previous_order = self.photoset.get_photo_order()
		inst = super(Photo, self).save(*args, **kwargs)
		if is_new:
			new_order = [self.pk] + previous_order
			self.photoset.set_photo_order(new_order)
		return inst
	
	def get_absolute_url(self):
		return reverse('clickclick.photo', args=[self.photoset.owner.username, self.photoset.slug, self.slug])
	
	def __unicode__(self):
		return self.title if self.title else self.slug
	
	class Meta:
		unique_together = ('photoset', 'slug',)
		ordering = ('_order',)
		order_with_respect_to = 'photoset'