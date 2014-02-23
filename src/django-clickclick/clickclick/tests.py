from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test.client import Client
from django.utils import unittest
from clickclick.models import Photo, PhotoSet


class TestPhotosetNavigation(unittest.TestCase):
	"""Tests the get_previous and get_next methods of the photo model."""
	
	def setUp(self):
		self.photoset = PhotoSet.objects.create(title="Test Set", slug="test-set")
		self.photo1 = Photo.objects.create(title="Photo 1", slug="photo1", photoset=self.photoset, index=1)
		self.photo2 = Photo.objects.create(title="Photo 2", slug="photo2", photoset=self.photoset, index=2)
		self.photo3 = Photo.objects.create(title="Photo 3", slug="photo3", photoset=self.photoset, index=3)
	
	def tearDown(self):
		self.photoset.delete()
		self.photo1.delete()
		self.photo2.delete()
		self.photo3.delete()
	
	def testNext(self):
		self.assertEqual(self.photo1.get_next(), self.photo2)
		self.assertEqual(self.photo2.get_next(), self.photo3)
		self.assertEqual(self.photo3.get_next(), None)
	
	def testPrevious(self):
		self.assertEqual(self.photo1.get_previous(), None)
		self.assertEqual(self.photo2.get_previous(), self.photo1)
		self.assertEqual(self.photo3.get_previous(), self.photo2)

class TestPhotosetCreationDeletion(unittest.TestCase):
	"""Tests the ability to create and delete PhotoSets."""
	
	def setUp(self):
		"""Creates two user accounts and a web client."""
		self.alice = User.objects.create_user('alice', 'alice@example.com', password='password')
		self.bob = User.objects.create_user('bob', 'bob@example.com', password='password')
		self.alice_client = Client()
		self.bob_client = Client()
		self.alice_client.login(username='alice', password='password')
		self.bob_client.login(username='bob', password='password')
	
	def tearDown(self):
		"""Deletes the two user accounts."""
		self.alice_client.logout()
		self.bob_client.logout()
		self.alice.delete()
		self.bob.delete()
	
	def testCreationDeletion(self):
		"""Checks that Alice can login and create and delete a PhotoSet."""
		# check that the photoset does not exist yet
		self.assertEqual(PhotoSet.objects.filter(slug='alices-photos').count(), 0)
		# create a photoset
		response = self.alice_client.post(reverse('clickclick.create_photoset'), {'title': 'Alice\'s Photos', 'slug': 'alices-photos', })
		# check that it exists
		self.assertEqual(PhotoSet.objects.filter(slug='alices-photos').count(), 1)
		# attempt to delete the photoset as bob
		response = self.bob_client.post(reverse('clickclick.delete_photoset', args=['alices-photos',]))
		# check that the photoset still exists (i.e., deletion failed)
		self.assertEqual(PhotoSet.objects.filter(slug='alices-photos').count(), 1)
		# delete the photoset as alice
		response = self.alice_client.post(reverse('clickclick.delete_photoset', args=['alices-photos',]))
		# check that it no longer still exists
		self.assertEqual(PhotoSet.objects.filter(slug='alices-photos').count(), 0)