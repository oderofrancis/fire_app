from django.shortcuts import render
from .forms import *
from django.contrib import messages

# Create your views here.

def home(request):
	return render(request,'report/home.html')

def report(request):

	form = IncidenceForm()

	if request.method =='POST':
		form =  IncidenceForm(request.POST)
		if form.is_valid():
			form.save()

			messages.success(request, 'we are working on the incidence reported,THANK YOU.')
			return redirect('/')

		else:

			messages.warning(request, form.errors)
			return redirect('/report/')


	context={'form':form}

	return render(request,'report/report.html',context)