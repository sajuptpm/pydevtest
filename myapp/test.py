

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
		self.data = {"name": "YPF, Luis Mar\u00eda Drago, El Tri\u00e1ngulo, Partido de Malvinas Argentinas, Bs. As., 1.619, Argentina", "datetime": "2018-07-02 11:24:57"}
		keystone_client.Client.return_value = mock.MagicMock(data)

		self.lat = '-34.4391708'
		self.lon = '-58.7064574'

	def test_get_address(self):
		c = Client()
		response = c.get(NOMINATIM_URL.format(lat=self.lat,lon=self.lon)
		self.assertEqual(response.json(), self.data)
