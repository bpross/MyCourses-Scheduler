# test for professor.py
# Author: Erik Steggall

"""
This file tests professor and course classes for our algorithm
"""

from professor import Professor
from course import Course

#Initializes Variables to be used
num = 0
num2 = 0
name = 's'
name2 = 's'
c_id = 0
c_name = 's'


# Test for constructors

# Test constructor with valid information
# Input: ID = 24 Name = Werner
# Expected output: (24, Werner)
p1 = Professor(24, 'Werner')
p1.print_professor()
# Test constructor, and add variables later
p2 = Professor()

# Add variables using manipulation procedure
p2.add_id(42)
p2.add_name('name')

# Test access functions using variables initialized above
num = p1.get_id()
name = p1.get_name()
num2 = p2.get_id()
name2 = p2.get_name()

# Print statment to insure that the variables 
print "Professors name is %s,\n professor's ID is %d" % (name, num)
print "Professors name is %s,\n professor's ID is %d" % (name2, num2)
p1.print_professor()

c1 = Course(84, 'CMPS')
c2 = Course()
c2.add_id(48)
c2.add_name('CMPE')

c_id = c1.get_id()
c_name = c1.get_name()

print "Course name is %s,\n course ID is %d" % (c_name, c_id)
c2.print_course()

p1.add_course(c1)
p1.add_course(c2)

for course in p1.course_list:
	course.print_course()
