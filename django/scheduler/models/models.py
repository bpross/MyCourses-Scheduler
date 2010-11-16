# CMPS 115 SCORE project
# Prof: Linda Werner
# 11-15-10


from django.db import models

class Professor(models.Model):
	id = models.IntegerField()
	name = models.CharField(max_length=50)

class Course(models.Model):
	id = models.IntegerField()
	name = models.CharField(max_length=50)

class Room(models.Model):
	seat_num = models.IntegerField()
	lab = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	requires_lab = models.IntegerField()


class Course_Class(models.Model):
	professor = models.ForeignKey(Professor)
	course = models.ForeignKey(Course)
	num_seats = models.IntegerField()
	requires_lab = models.IntegerField()
	duration = models.IntegerField()
