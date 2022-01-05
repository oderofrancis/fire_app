from django import forms
from django.contrib.gis import forms as geoforms
from django.forms import ModelForm
from .models import *


class IncidenceForm(geoforms.ModelForm):

    class Meta:
        model = Incidence
        fields = ('place','injuries','location')
        widgets = {'location':  geoforms.OSMWidget(
        	attrs={
        	'map_width': 330, 
        	'map_height': 500,
        	'default_lat':  -0.42768,
            'default_lon': 36.9580,
    		'default_zoom':6,
    		'max_zoom':20,
    		'min_zoom':3,
    		
        	})}