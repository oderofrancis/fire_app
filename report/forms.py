from django import forms
from django.contrib.gis import forms as geoforms
from django.forms import ModelForm
from .models import *


class IncidenceForm(forms.ModelForm):

    class Meta:
        model = Incidence
        fields = ('place','injuries','location')
        
        widgets = {'location':  geoforms.OSMWidget(
        	attrs={
        	'map_width': 330, 
        	'map_height': 400,
        	'default_lat':  -0.42768,
            'default_lon': 36.9580,
    		'default_zoom':9.5,
    		'max_zoom':20,
    		'min_zoom':5,
    		
        	})}