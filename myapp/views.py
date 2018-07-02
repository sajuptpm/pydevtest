# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.cache import cache
from django.conf import settings
from django.http import JsonResponse
import datetime
import base64
import json
from .utils import _get_data_from_nominatim


# Create your views here.

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def get_address(request, lat, lon):
	key = encoded = base64.b64encode(lat+lon)
	cach_data = cache.get(key)
	if not cach_data:
		data = _get_data_from_nominatim(lat, lon)
		if data:
			cache.set(key, json.dumps(data))
	else:
		data = json.loads(cach_data)
		cached_datetime =  data.get('datetime')
		_cached_datetime = datetime.datetime.strptime(cached_datetime, DATE_FORMAT)
		diff_date = datetime.datetime.now() - _cached_datetime
		if diff_date.seconds >= 86400:
			data = _get_data_from_nominatim(lat, lon)
			cache.set(key, json.dumps(data))
	if data:
		return JsonResponse({'name': data})
	else:
		return JsonResponse({'Error': "Data not Found"})




