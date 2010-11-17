#!/usr/local/bin/python
#Author: Benjamin Ross(bpross)
#Date: 11/10

"""
Tests the configuration class
"""

from configuration import Configuration

config = Configuration()

test = config.is_empty()
print test

config.parse_file('config')

test = config.is_empty()
print test

num = config.get_num_prof()
print num

prof = config.get_professor_by_id(4)
prof.print_professor()

num = config.get_num_course()
print num

course = config.get_course_by_id(5)
print str(course.id) + " " + course.name

num = config.get_num_rooms()
print num

room = config.get_room_by_id(2)
print str(room.name) + " " + str(room.seat_num) + " " + str(room.lab)

num = config.get_num_classes()
print num

t_class = config.get_class_by_course(2)
prof = config.get_professor_by_id(t_class.professor)
prof.print_professor()
