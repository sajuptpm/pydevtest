

from django.test import TestCase
from django.test import Client
from django.conf import settings
import requests
import mock

NOMINATIM_URL = getattr(settings, "NOMINATIM_URL", None)

class GetAddressTestCase(TestCase):
	def setUp(self):
		super(GetAddressTestCase, self).setUp()
		self.patch_requests_get= mock.patch.object(requests, 'get')
		self.patch_requests_get.start()
		data = {}
		keystone_client.Client.return_value = mock.MagicMock(data)

		self.lat = '-34.4391708'
		self.lon = '-58.7064573'

	def test_get_address(self):
		c = Client()
		response = c.get(NOMINATIM_URL.format(lat=self.lat,lon=self.lon)
		#response.json()['name']
		#self.assertEqual(response.content, b"Bienvenue sur mon site.")
		#https://docs.djangoproject.com/en/2.0/topics/testing/tools/
