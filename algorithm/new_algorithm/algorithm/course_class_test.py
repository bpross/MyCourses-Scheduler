#!/usr/bin/local/python
#Author: Benjamin Ross(bpross)

"""
Tests the CourseClass class
"""

from course_class import CourseClass
from professor import Professor
from course import Course

p1 = Professor(24, 'Werner')
p2 = Professor(25, 'Tantalo')
c1 = Course(24, 'CMPS 115')
c2 = Course(25, 'CMPS 101')

cc1 = CourseClass(p1,c1,25,False,1)
print cc1

cc2 = CourseClass()
print cc2

cc2.add_professor(p2)
print cc2.get_professor()

cc2.add_course(c2)
print cc2.get_course()

cc2.add_seats(80)
print cc2.get_room_size()

cc2.add_lab(True)
print cc2.needs_lab()

cc2.add_duration(1)
print cc2.get_duration()
