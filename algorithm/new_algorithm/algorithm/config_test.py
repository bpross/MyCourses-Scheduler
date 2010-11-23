#!/usr/local/bin/python
#Author: Benjamin Ross(bpross) 
#Author: Justin Lazaro(jlazaro)
#Date: 11/10

"""
This is a unit test of configuration.py
This tests various functions in the configuration class
"""
from configuration import Configuration

config = Configuration()


"""
This is testing the is_empty() function in configuration.py
It checks to see if the config file is empty 
Input: config file
Expected output: False 
"""
test = config.is_empty()
print test

config.parse_file('config')

test = config.is_empty()
print test


"""
This is testing the get_num_prof() function in  configuration.py
It checks to see if the config file returns the correct number of professors
Input: config file (13 professors)
Expected output: 13
"""
num = config.get_num_prof()
print num


"""
This is testing the get_professor_by_id() and print_professor() functions in configuration.py
It checks to see the config file returns the correct professor by ID number
Input: config file (ID: 4)
Expected output: (4,Marry)
"""
prof = config.get_professor_by_id(4)
prof.print_professor()


"""
This is testing the get_num_course() function in configuration.py
It checks to see if the correct number of courses is returned
Input: config file (8 courses) 
Expected output: 8 (courses) 
"""
num = config.get_num_course()
print num


"""
This is testing the get_course_by_id() function in configuration.py
It checks to see if the correct course ID and course name
Input: config file (ID: 5)
Expected output: 5 Descrete Mathematic I
""""
course = config.get_course_by_id(5)
print str(course.id) + " " + course.name


"""
This is testing the get_num_rooms() function in configuration.py
It checks to see if the correct number of rooms is returned
Input: config file (3 rooms)
Expected output: 3
"""
num = config.get_num_rooms()
print num


"""
BEN This test case does not look correct, it seems like you don't have an ID number under rooms in your config file

This is testing the get_room_by_id() function in configuration.py
It checks to see if the correct room name, seat number, and lab is returned 
Input: config file (ID: 2)
Expected output: Unknown
"""
room = config.get_room_by_id(2)
print str(room.name) + " " + str(room.seat_num) + " " + str(room.lab)


"""
This is testing the get_num_classes() function in configuration.py
It checks to see if the correct number of classes is returned 
Input: config file(26 classes)
Expected output: 26 
"""
num = config.get_num_classes()
print num


"""
This is testing the get_class_by_course() function
Input: config file
Expected output: 2
This is testing the get_professor_by_id() function
Input: t_class.professor
Expected output: (Professor IDs) 2 and 3
This is testing the print_professor() function
Input: prof
Expected output: (2, Red) (3, Philip)
"""
t_class = config.get_class_by_course(2)
prof = config.get_professor_by_id(t_class.professor)
prof.print_professor()
