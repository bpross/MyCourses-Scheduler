#Course Scheduling Algorithm
#CMPS 115
#Linda Werner
#course.py


import sys

class Course:

 	id = 0
        name = ''
        #initializes course with ID and name
	def __init__(self, id, name = None):
		self.id = id
                self.name = name

	#prints out the course data
	def print_course(self):
		print "(%d, %s)" % (self.id, self.name)


if __name__ == '__main__':

	p1 = Course(115, "SoftwareDesign")
	p1.print_course()
	sys.exit(0)

