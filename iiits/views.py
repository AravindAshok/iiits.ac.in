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

class FacultyPageView(TemplateView):
	template_name = 'iiits/faculty/faculty_page.html'
	def get_context_data(self, **kwargs):
		context = super(FacultyPageView,self).get_context_data(**kwargs)
		context = dict()
		
		dept=self.request.GET.get('dept')
		title=self.request.GET.get('title')
		ra=self.request.GET.get('ra')
		vs=self.request.GET.get('vs')
		instfac = self.request.GET.get('instfac')
		
		fac = FacultySearch(dept=dept,title=title,ra=ra,vs=vs,instfac=instfac)
		faculty=fac.search()

		context['faculty'] = faculty
		return context

class FacultyProfileView(TemplateView):
	template_name='iiits/faculty/faculty_profile.html'
	def get_context_data(self, **kwargs):
		context = super(FacultyProfileView,self).get_context_data(**kwargs)	
		context=dict()
		context['path']=self.request.path
		return context

