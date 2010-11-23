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
# Test constructor with low number bound
# Input: ID = 0, Name = Werner
# Expected output: (0, Werner)
p1 = Professor(0, 'Werner')
p1.print_professor()
# Test constructor with No name input
# Input: ID = 24, Name = 
# Expected output: (24, )
p1 = Professor(24, '')
p1.print_professor()
# Test constructor with high number bound
# Input: ID = 24000000000000000000, Name = Werner
# Expected output: (24000000000000000000, Werner)
p1 = Professor(24000000000000000000, 'Werner')
p1.print_professor()
# Test constructor with no ID
# Input: ID = \0, Name = Werner
# Expected output: Should throw error message
p1 = Professor(Werner)
# Test constructor with no name
# Input: ID = 24, Name = \0
# Expected output: should throw error message
p1 = Professor(24)
p1.print_professor()
# Test constructor, and add variables later
p2 = Professor()

# Add variables using manipulation procedure
p2.add_id(42)
p2.add_name('name')

# Test for invalid manipulations
p3 = Professor()
# Input: ID = name
# Expected output: Should throw error message
p3.add_id('name')
# Input: Name = 24
# Expected output: Should throw error message
p3.add_name(24)

# Test access functions using variables initialized above
num = p1.get_id()
name = p1.get_name()
num2 = p2.get_id()
name2 = p2.get_name()

# Print statment to insure that the variables 
print "Professors name is %s,\n professor's ID is %d" % (name, num)
print "Professors name is %s,\n professor's ID is %d" % (name2, num2)
p1.print_professor()

