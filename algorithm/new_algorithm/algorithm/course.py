#Course Scheduling Algorithm
#CMPS 115
#Linda Werner
#course.py
#Authors: egall24, bpross

import sys

class Course:

 	id = 0
        name = ''
        #initializes course with ID and name
	def __init__(self, id, name = None):
		if id is None:
			self.id = None
		else:
			self.id = id
		if name is None:
			self.id = None
		else:
			self.name = name

	#Returns the id of the course
	def get_id(self):
		return self.id

	#Adds/Changes ID of the course
	def add_id(self,id):
		self.id = id

	#Adds/changes name of the course
	def add_name(self,name):
		self.name = name
		
	#Returns the name of the course
	def get_name(self):
		return self.name
	
	#prints out the course data
	def print_course(self):
		print "(%d, %s)" % (self.id, self.name)


if __name__ == '__main__':

	p1 = Course(115, "SoftwareDesign")
	p1.print_course()
	sys.exit(0)

