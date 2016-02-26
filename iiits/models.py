from __future__ import unicode_literals

from django.db.models import *
from django.contrib.auth.models import User
class Department(Model):
	name = CharField(max_length=100)
	code = CharField(max_length=20)
class FacultyTitle(Model):
	title = CharField(max_length=100)
	code = CharField(max_length=20)
class ResearchArea(Model):
	title = CharField(max_length=150)
	code = CharField(max_length=50)
	
class Faculty(Model):
	user = OneToOneField(User)
	photo=ImageField()
	title = ForeignKey(FacultyTitle)
	research_areas = CommaSeparatedIntegerField(max_length=150)#ResearchArea IDs
	department = ForeignKey(Department)
	contact_no=TextField()
	professional_edu=TextField()
	website=TextField()
	
class Publications(Model):
	title= CharField(max_length=200)
	description=TextField()
	link=TextField()
	fileupload = FileField()
	year=CharField(max_length=4)	
	starred=BooleanField(default=False)
	

'''
class Staff(Model):
class UGStudent(Model):
class PGStudent(Model):
class DoctoralStudent(Model):
class ResearchScholar(Model):
class Alumni(Model):
class 
'''
