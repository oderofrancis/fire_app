from django.shortcuts import render
from .forms import *

# Create your views here.

def home(request):
	return render(request,'report/home.html')

def report(request):

	form = IncidenceForm()

	if request.method =='POST':
		form =  IncidenceForm(request.POST)
		if form.is_valid():
			form.save()


	context = {'form':form}

	return render(request,'report/report.html',context)