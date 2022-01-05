from django.contrib import admin
from .models import *
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class IncidenceAdmin(LeafletGeoAdmin):

	list_display = ['place','injuries','location','date_reported']

admin.site.register(Incidence,IncidenceAdmin)