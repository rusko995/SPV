import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Album, Picture

class AlbumTests(TestCase):
	def testIsRecentlyPublished(self):
		"""	is_recently_published() should return True, if the publish date is recent;
		False otherwise.
		"""
		a_recent = Album(title='test_recent', pubDate=timezone.now())
		a_old = Album(title='old', pubDate=timezone.now()-datetime.timedelta(days=6))

		self.assertIs(a_recent.was_published_recently(), True)
		self.assertIs(a_old.was_published_recently(), False)

	def hasCover(self):
		"""has_cover should return True, if album has cover photo
		False otherwise
		"""

		a_has = Album (title='ima' , naslovnaSlika='static/testnaSlika.png')
		a_not = Album (title='nima', naslovnaSlika=None)

		self.assertIs(a_has.has_cover_photo(), True)
		self.assertIs(a_not.has_cover_photo(), False)
	
	
class PictureTests(TestCase):
	def testFilename(self):
		"""tests if default value for title is correctly set"""
		lala='test'
		a_ima = Picture(title=lala)
		a_nima = Picture()

		self.assertIs(a_ima.get_image_filename(), lala)
		self.assertIs(a_nima.get_image_filename(), '')
		