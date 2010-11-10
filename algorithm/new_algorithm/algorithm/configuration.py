#!/usr/local/bin/python
#Author: Benjamin Ross(bpross)
#Date: 10/25

"""
This is being modified from code provided by Mladen Jankovic on
http://www.thecodeproject.com. His full source code and license is included with these files.

This reads in a configuration file and stores the parsed objects
"""

class Configuration:
    
    def __init__(self,prof_list = None, course_list = None,
                 room_list = None, classes_list = None):
        if prof_list is None:
            self.prof_list = None
        else:
            self.prof_list = prof_list
        if course_list is None:
            self.course_list = None
        else:
            self.course_list = course_list
        if room_list is None:
            self.room_list = None
        else:
            self.room_list = room_list
        if classes_list = None:
            self.classes_list = None
        else:
            self.classes+list = classes_list

        self.is_empty = True
        self.num_professors = 0
        self.num_rooms = 0
        self.num_classes = 0
        self.num_courses = 0


    def is_empty(self):
        return self.is_empty

    #Returns the professor with specified ID
    #If there is no professor with such ID method returns False
    def get_professor_by_id(self,id):

        for professor in self.prof_list:
            new_id = professor.get_id()
            if new_id is id:
                return professor

        #Not in list
        return False

    #Returns the number of parsed professors
    def get_num_prof(self):
        return self.num_professors

    #Returns the course with specified ID
    #If there is no course with such ID method returns False
    def get_course_by_id(self, id):

        for course in self.course_list:
            new_id = course.get_id()
            if new_id is id:
                return course

        #Not in list
        return False

    #Returns the number of parses courses
    def get_num_course(self):
        return self.num_courses

    #Returns the room with specified ID
    #If there is no room with such ID method returns False
    def get_room_by_id(self, id):

        for room in self.room_list:
            new_id = room.get_id()
            if new_id is id:
                return room

        #Not in List
        return false

    #Returns the number of parsed rooms
    def get_num_rooms(self):
        return self.num_rooms

    #Returns the class with specified ID
    #IF there is no class with such ID method returns False
    def get_class_by_id(self,id):

        for class in self.class_list:
            new_id = class.get_id()
            if new_id is id:
                return class

        #Not in list
        return false

    #Returns the number of parsed classes
    def get_num_classes(self):
        return self.num_classes

    #Parses the file and stores the prased objects
    def parse_file(self,file):

        f = open(file, 'r')
        file_list = file.readlines()

        for lines in range(len(file_list)):

            #Tokenizes the string
            line = file_list[lines].split()

            if 'prof' in line[0]:
                parse_prof(self,file_list[lines:lines+2])
            elif 'course' in line[0]:
                parse_course(self,file_list[lines:lines+2])
            elif 'class' in line[0]:
                parse_class(self,file_list[lines:lines+5])
            elif 'room' in line[0]:
                parse_room(self.file_list(lines:lines+3])

    #Reads professor's data from config file, adds object to list
    #Returns None if method cannot parse configuration data
    def parse_prof(self,line_list):

        self.prof_list.append(Professor())
        for line in range(len(line_list)):
            words = line_list[line].split()

            #Parse ID
            if 'id' in words[0]:
                
        
        