# CMPS 194 business plan project
# Prof: Charlie McDowell
# 03-01-11

from django.db import models
from django.contrib import admin


# Business
class Business(models.Model):
	business_name = models.CharField(max_length=45, primary_key=True)
	id = models.IntegerField(unique=True)
	class Meta:
		verbose_name_plural = "Businesses"

	def __unicode__(self):
	  return self.business_name

class BusinessAdmin(admin.ModelAdmin):
	list_display = ('business_name', 'id')
	search_fields = list_filter = list_display_links = list_display

  
# Building:
class Building(models.Model):
	idBuilding = models.IntegerField(primary_key=True)
	building_name = models.CharField(max_length=45)
	idBusiness = models.ForeignKey(Business, to_field='business_name')

	def __unicode__(self):
		return self.building_name
		
class BuildingAdmin(admin.ModelAdmin):
	list_display = ('idBuilding', 'building_name', 'idBusiness')
	list_display_links = ('idBuilding', 'building_name', 'idBusiness')
	list_filter = ('idBuilding', 'building_name', 'idBusiness')
	search_fields = ('idBuilding', 'building_name', 'idBusiness')
	# This is not user-friendly. If possible, we should list idBusiness by associated Business_name.

# Employer
class Employer(models.Model):
	idEmployer = models.IntegerField(primary_key=True)
	employer_name = models.CharField(max_length=45)
	idBusiness = models.ForeignKey(Business, to_field='business_name')

	def __unicode__(self):
		return self.employer_name  

class EmployerAdmin(admin.ModelAdmin):
	list_display = ('idEmployer', 'employer_name', 'idBusiness')
	list_display_links = ('idEmployer', 'employer_name', 'idBusiness')
	list_filter = ('idEmployer', 'employer_name', 'idBusiness')
	search_fields = ('idEmployer', 'employer_name', 'idBusiness')

# Position
class Position(models.Model):
	position_name = models.CharField(max_length=45, unique=True)
	# Unique should be FALSE. This is a BAD HACK to validate our models for now.
	idBusiness = models.ForeignKey(Business, to_field='business_name')
	def __unicode__(self):
		return u'%s' % (self.position_name)

class PositionAdmin(admin.ModelAdmin):
	list_display = ('position_name', 'idBusiness')
	list_display_links = ('position_name', 'idBusiness')
	list_filter = ('position_name', 'idBusiness')
	search_fields = ('position_name', 'idBusiness')

# Employee
class Employee(models.Model):
	idEmployee = models.IntegerField(primary_key=True)
	employee_first_name = models.CharField(max_length=45)
	employee_middle_name = models.CharField(max_length=45)
	employee_last_name = models.CharField(max_length=45)
	employee_position = models.CharField(max_length=45)
	employee_availability = models.DateTimeField(auto_now=False, auto_now_add=False)
	employee_start_date = models.DateField()
	employee_end_date = models.DateField()
	employee_medical_conditions = models.CharField(max_length=15)
	employee_email = models.EmailField(max_length=75)
	employee_phone_number = models.IntegerField(null=True)
	employee_wage = models.IntegerField(null=True)
	employee_education = models.CharField(max_length=45)
	employee_professional_skills = models.TextField()
	employee_employed = models.BooleanField(default=False)
	employee_position = models.ForeignKey(Position, to_field='position_name')
	idBusiness = models.ForeignKey(Business, to_field='business_name')

	def __unicode__(self):
		return u'%s %s %s' % (self.employee_last_name, self.employee_middle_name, self.employee_last_name)

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('idEmployee', 'employee_first_name', 'employee_middle_name', 'employee_position', 'employee_availability', 'employee_start_date', 'employee_end_date', 'employee_medical_conditions', 'employee_email', 'employee_phone_number', 'employee_wage', 'employee_education', 'employee_professional_skills', 'employee_employed', 'employee_position', 'idBusiness')
	list_display_links = ('idEmployee', 'employee_first_name', 'employee_middle_name', 'employee_position', 'employee_availability', 'employee_start_date', 'employee_end_date', 'employee_medical_conditions', 'employee_email', 'employee_phone_number', 'employee_wage', 'employee_education', 'employee_professional_skills', 'employee_employed', 'employee_position', 'idBusiness')
	list_filter = ('idEmployee', 'employee_first_name', 'employee_middle_name', 'employee_position', 'employee_availability', 'employee_start_date', 'employee_end_date', 'employee_medical_conditions', 'employee_email', 'employee_phone_number', 'employee_wage', 'employee_education', 'employee_professional_skills', 'employee_employed', 'employee_position', 'idBusiness')
	search_fields = ('idEmployee', 'employee_first_name', 'employee_middle_name', 'employee_position', 'employee_availability', 'employee_start_date', 'employee_end_date', 'employee_medical_conditions', 'employee_email', 'employee_phone_number', 'employee_wage', 'employee_education', 'employee_professional_skills', 'employee_employed', 'employee_position', 'idBusiness')
	
