#Course Scheduling Algorithm
#CMPS 115
#Linda Werner
#professor.py

import sys

class Professor:
 	id = 0
        name = ''
        #initializes professor with ID and name
	def __init__(self, id, name = None):
		self.id = id
                self.name = name

	#prints out the professors data
	def print_professor(self):
		print "(%d, %s)" % (self.id, self.name)


if __name__ == '__main__':

	p1 = Professor(24, "Werner")
	p1.print_professor()
	sys.exit(0)



