from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.core.serializers import serialize
import geopandas as gpd

# Create your views here.

def home(request):
	return render(request,'report/home.html')

def report(request):

	form = IncidenceForm()

	if request.method == 'POST':
  		form = IncidenceForm(request.POST)
  		if form.is_valid():
  			form.save()

  			messages.success(request, 'we are working on the incidence reported,THANK YOU.')
  			return redirect('/')

  		else:
  			messages.warning(request, form.errors)
  			return redirect('/report/')


	# for the values

	cases = Incidence.objects.all().count()
	values = Incidence.objects.all()
	values = serialize('geojson',values)
	values = gpd.read_file(values)
	values = values[values.columns[1]].sum()


	context={'form':form,'cases':cases,'values':values}

	return render(request,'report/report.html',context)


def loginPage(request):
	return render(request,'analysis/login.html')

def registerPage(request):
	return render(request,'analysis/register.html')

def dashboard(request):
	return render(request,'analysis/dashboard.html')