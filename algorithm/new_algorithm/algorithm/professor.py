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
			sself.course_list = course_list


	#Returns the professor's ID
	def get_id(self):
		return self.id

	#Returns the professor's name
	def get_name(self):
		return self.name

	#Returns the professor's course list
	def get_courses(self):
		return self.course_list
	
	#prints out the professors data
	def print_professor(self):
		print "(%d, %s)" % (self.id, self.name)


if __name__ == '__main__':

	p1 = Professor(24, "Werner")
	p1.print_professor()
	sys.exit(0)



