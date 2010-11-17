# CMPS 115 SCORE project
# Prof: Linda Werner
# 11-15-10


from django.db import models

class Professor(models.Model):
	id = models.IntegerField()
	name = models.CharField(max_length=50)

	__metaclass__ = models.SubfieldBase

	def __unicode__(self):
		return self.name

class Course(models.Model):
	id = models.IntegerField()
	name = models.CharField(max_length=50)

	__metaclass__ = models.SubfieldBase

	def __unicode__(self):
		return self.name

class Buildings(Course):
	name = models.CharField(max_length=50)

	__metaclass__ = models.SubfieldBase

	def __unicode__(self):

class Room(models.Model):
	seat_num = models.IntegerField()
	lab = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	requires_lab = models.BooleanField()

	__metaclass__ = models.SubfieldBase

	def __unicode__(self):
		return self.name


class Course_Class(models.Model):
	professor = models.ForeignKey(Professor)
	course = models.ForeignKey(Course)
	num_seats = models.IntegerField()
	requires_lab = models.BooleanField()
	duration = models.IntegerField()

	__metaclass__ = models.SubfieldBase

	def __unicode__(self):
		return self.name

class Master_table(models.Model):
	professor = models.ManyToMany(Professor)
	room = models.ManyToMany(Room)
	course = models.ManyToMany(Course)

	__metaclass__ = models.SubfieldBase

	def __unicode__(self):
		return self.name 
	
class Person(models.Model):
	first_name = models.CharField(max_lenght=50)
	minitial = models.CharField(max_length=1)
	last_name = models.CharField(max_length=50)
	suffix = models.CharField(max_length=50)
	prefix = modles.CharField(max_length=50)

	__metaclass__ = models.SubfieldBase

	def __unicode__(self):
		return self.name 
	

class School(models.Model):
	school = models.CharField(max_length=50)

	__metaclass__ = models.SubfieldBase

	def __unicode__(self):
		return self.name 
	
class Department(models.Model):
	department = modles.CharField(max_lenght=50)
	dep_abbrev = models.CharField(max=length=4)
	chair_id = models.ForeignKey(Chair)
	school_id = models.ForeignKey(School)

	__metaclass__ = models.SubfieldBase

	def __unicode__(self):
		return self.name

    
	


	




