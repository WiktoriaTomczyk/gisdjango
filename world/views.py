from django.shortcuts import render
from .models import WorldBorder
from django.core.serializers import serialize

def index(request, fips):
    border = WorldBorder.objects.filter(fips=fips.upper())
    fields=('name', 'area', 'pop2005', 'region', 'subregion', 'lon', 'lat')
    geojson = serialize('geojson', border, geometry_field='geom', fields=fields)
    return render(request, 'world/index.html', { 'border': geojson })

