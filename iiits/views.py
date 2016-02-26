from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView, View
from django.conf import settings
from iiits.models import *
from iiits.methods import *
from iiits.algorithms import *

class HomeView(TemplateView):
	template_name = 'iiits/index.html'
	
	def get_context_data(self, **kwargs):
		
		context = super(HomeView,self).get_context_data(**kwargs)
		context = {

		}
		
		return context

class FacultyView(TemplateView):
	template_name = 'iiits/faculty/faculty_home.html'
	def get_context_data(self, **kwargs):
		context = super(FacultyView,self).get_context_data(**kwargs)
		context = dict()

		return context		

class FacultyProfileView(TemplateView):
	template_name = 'iiits/faculty/faculty_profile.html'
	def get_context_data(self, **kwargs):
		context = super(FacultyProfileView,self).get_context_data(**kwargs)
		context = dict()
		dept=self.request.GET.get('dept')
		ifNone(dept,'all')
		title=self.request.GET.get('title')
		ifNone(title,'all')
		ra=self.request.GET.get('ra')
		ifNone(ra, 'all')
		vs=self.request.GET.get('vs')
		ifNone(vs,'true')
		instfac = self.request.GET.get('instfac')
		ifNone(instfac,'true')
		
		return context		
