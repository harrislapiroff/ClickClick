from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class PhotoSet(models.Model):
	"""A photoset with photos in it."""
	title = models.CharField(max_length=100)
	slug = models.CharField(max_length=50, unique=True)
	description = models.TextField(blank=True)
	owner = models.ForeignKey(User, null=True, related_name='photosets')
	creation_time = models.DateTimeField(auto_now_add=True)
	last_updated_time = models.DateTimeField(auto_now=True)
	
	def get_absolute_url(self):
		return reverse('clickclick.photoset', args=[self.slug])
	
	def __unicode__(self):
		return self.title


class Photo(models.Model):
	"""A photo with metadata, which ideally belongs to a photoset. However, it is possible for a photo not to belong to a photoset, and therefore the owner property is necessary."""
	title = models.CharField(max_length=128, blank=True)
	slug = models.CharField(max_length=128)
	owner = models.ForeignKey(User, null=True, related_name="photos")
	image = models.ImageField(upload_to='photos')
	caption = models.TextField(blank=True)
	photoset = models.ForeignKey(PhotoSet, related_name='photos')
	index = models.PositiveIntegerField(default=0)
	upload_time = models.DateTimeField(auto_now_add=True)
	last_updated_time = models.DateTimeField(auto_now=True)
	
	def get_absolute_url(self):
		return reverse('clickclick.photo', args=[self.photoset.slug, self.slug])
	
	def __unicode__(self):
		return self.title if self.title else self.slug
	
	class Meta:
		unique_together = ('photoset', 'slug',)
		ordering = ('index', '-upload_time')