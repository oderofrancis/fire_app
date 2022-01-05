from django.urls import path
from .views import *

urlpatterns = [
	path('',home,name='home'),
	path('report/',report,name='report'),
	path('login/',loginPage,name='login'),
	path('register/',registerPage,name='register'),
	path('dashboard/',dashboard,name='dashboard'),

]