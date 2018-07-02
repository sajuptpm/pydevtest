
from django.core.cache import cache
from django.conf import settings
import requests
import datetime
import json

NOMINATIM_URL = getattr(settings, "NOMINATIM_URL", None)
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def _get_data_from_nominatim(lat, lon):
	data = {}
	try:
		res = requests.get(NOMINATIM_URL.format(lat=lat,lon=lon))
	except requests.exceptions.Timeout as ex:
		##Logging
		pass
	if res.status_code == requests.codes.ok:
		_data = res.json()
		display_name = _data.get('display_name')
		#data.get('address', {}).get('postcode')
		data = {'datetime' : datetime.datetime.now().strftime(DATE_FORMAT), 'name': display_name}
	return data




#python manage.py createcachetable
#http://127.0.0.1:8000/myapp/get_address/-34.4391708/-58.7064573/


