from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^(?P<fips>\w+)$', views.index, name='index')
]
