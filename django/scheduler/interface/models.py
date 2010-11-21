# CMPS 115 SCORE project
# Prof: Linda Werner
# 11-15-10


from django.db import models

class Professor(models.Model):
	ProfessorID = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Course(models.Model):
	CourseID = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Buildings(models.Model):
	name = models.CharField(max_length=50)
	BuildingID = models.IntegerField(primary_key=True)

	def __unicode__(self):
		return self.name

class Room(models.Model):
	seat_num = models.IntegerField()
	BuildingID = models.ForeignKey('Buildings', to_field="BuildingID")
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name


class Course_Class(models.Model):
	professor = models.ForeignKey('Professor')
	course = models.ForeignKey('Course')
	num_seats = models.IntegerField()
	requires_lab = models.BooleanField()
	duration = models.IntegerField()

	def __unicode__(self):
		return self.name

class Master_table(models.Model):
	professor = models.ManyToManyField('Professor')
	room = models.ManyToManyField('Room')
	course = models.ManyToManyField('Course')

	def __unicode__(self):
		return self.name 
	
class Person(models.Model):
	first_name = models.CharField(max_length=50)
	minitial = models.CharField(max_length=1)
	last_name = models.CharField(max_length=50)
	suffix = models.CharField(max_length=50)
	prefix = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name 
	

class School(models.Model):
	school = models.CharField(max_length=50)	

	def __unicode__(self):
		return self.name 
	
class Department(models.Model):
	department = models.CharField(max_length=50)
	dep_abbrev = models.CharField(max_length=4)
	chair_id = models.ForeignKey('Person')
	school_id = models.ForeignKey('School')

	def __unicode__(self):
		return self.name