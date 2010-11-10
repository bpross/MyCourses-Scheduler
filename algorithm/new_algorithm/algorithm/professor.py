#Course Scheduling Algorithm
#CMPS 115
#Linda Werner
#professor.py
#Authors: egall24, bpross

import sys

class Professor:
	id = 0
	name = ''
	#initializes professor with ID and name
	def __init__(self, id = None, name = None,course_list = None):
		if id is None:
			self.id = None
		else:
			self.id = id
		if name is None:
			self.name = None
		else:
			self.name = name
		if course_list is None:
			self.course_list = None
		else:
			self.course_list = course_list
	#Returns the professor's ID
	def get_id(self):
		return self.id

	#Returns the professor's name
	def get_name(self):
		return self.name

	#Returns the professor's course list
	def get_courses(self):
		return self.course_list


	#Adds/changes ID of the professor
	def add_id(self,id):
		self.id = id

	#Adds/changes Name of the professor
	def add_name(self,name):
		self.name = name
		
	#Adds a course to the professor's list
	def add_course(self,course):
		if self.course_list is None:
			self.course_list = []
		self.course_list.append(course)
		
	#prints out the professors data
	def print_professor(self):
		print "(%d, %s)" % (self.id, self.name)

	def get_id(self):
		return self.id
	
	def get_name(self):
		return self.name

if __name__ == '__main__':
	num = 0
	str = 'Steggall'
	p1 = Professor(24, "Werner")
	p1.print_professor()
	id = p1.id
	p1name = p1.name
	print "(Professor's name is: %s ID is: %d)" % (p1name, id)
	num = p1.get_id()
	print "num should equal %d" % (num)
	str = p1.get_name()
	print "string should be %s" % (str)


	sys.exit(0)



