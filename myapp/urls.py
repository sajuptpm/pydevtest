from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_address/(?P<lat>-?\d+\.\d+)/(?P<lon>-?\d+\.\d+)/$', views.get_address, name='get_address'),
]
