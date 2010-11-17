#!/usr/local/bin/python
#Author: Benjamin Ross(bpross)
#Date: 10/25

"""
This is being modified from code provided by Mladen Jankovic on
http://www.thecodeproject.com. His full source code and license is included with these files.

This reads in a configuration file and stores the parsed objects
"""

from professor import Professor
from course_class import CourseClass
from room import Room
from course import Course

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
        if classes_list is None:
            self.classes_list = None
        else:
            self.classes_list = classes_list

        self.empty = True
        self.num_professors = 0
        self.num_rooms = 0
        self.num_classes = 0
        self.num_courses = 0


    def is_empty(self):
        return self.empty

    #Returns the professor with specified ID
    #If there is no professor with such ID method returns False
    def get_professor_by_id(self,id):

        for professor in self.prof_list:
            new_id = professor.get_id()
            if new_id is id:
                return professor

        #Not in list
        return None

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

    #Returns the room with specified id
    #If there is no room with such ID method returns False
    def get_room_by_id(self, id):

        for room in self.room_list:
            new_id = room.get_id()
            if new_id is id:
                return room

        #Not in List
        return False

    #Returns the number of parsed rooms
    def get_num_rooms(self):
        return self.num_rooms

    #Returns the class with specified course
    #IF there is no class with such ID method returns False
    def get_class_by_course(self,course_id):

        for new_class in self.classes_list:
            new_course = new_class.get_course()
            
            if new_course is course_id:
                return new_class

        #Not in list
        return False

    #Returns the number of parsed classes
    def get_num_classes(self):
        return self.num_classes

    #Parses the file and stores the prased objects
    def parse_file(self,file):

        f = open(file, 'r')
        file_list = f.readlines()

        lines = 0
        room_id = 1
        while lines in range (len(file_list)):
            
            #Tokenizes the string
            line = file_list[lines].split()
            
            if line:
                if 'prof' in line[0]:
                    lines = self.parse_prof(file_list,lines)
                elif 'course' in line[0]:
                    lines = self.parse_course(file_list,lines)
                elif 'class' in line[0]:
                    lines =  self.parse_class(file_list,lines)
                elif 'room' in line[0]:
                    lines = self.parse_room(file_list,lines,room_id)
                    room_id += 1

            lines += 1

        self.empty = False
        
    #Reads professor's data from config file, adds object to list
    def parse_prof(self,file_list,lines):

        if self.prof_list is None:
            self.prof_list = []
            
        self.prof_list.append(Professor())
        prof = self.prof_list[-1]

        line = file_list[lines]

        while 'end' not in line:
            #Parse ID
            if 'id' in line:
               words = line.split()
               prof.add_id(int(words[2]))

            #Parse Name
            elif 'name' in line:
                words = line.split()
                prof.add_name(words[2])

            lines += 1
            line = file_list[lines]

        self.num_professors += 1
        return lines
        
    #Reads course data from config file, adds object to list
    def parse_course(self,file_list,lines):

        if self.course_list is None:
            self.course_list = []
            
        self.course_list.append(Course())
        course = self.course_list[-1]

        line = file_list[lines]

        while 'end' not in line:
            #Parse ID
            if 'id' in line:
                words = line.split()
                course.add_id(int(words[2]))

            #Parse Name
            elif 'name' in line:
                words = line.split()
                course.add_name(words[2])

            lines += 1
            line = file_list[lines]

        self.num_classes += 1
        return lines
        
    #Reads class data from config file, adds object to list
    def parse_class(self,file_list,lines):

        if self.classes_list is None:
            self.classes_list = []
            
        self.classes_list.append(CourseClass())
        new_class = self.classes_list[-1]

        line = file_list[lines]

        while 'end' not in line:
            #Parse Professor
            if 'professor' in line:
                words = line.split()
                new_class.add_professor(int(words[2]))

            #parse Course
            elif 'course' in line:
                words = line.split()
                new_class.add_course(int(words[2]))

            #Parse Duration
            elif 'duration' in line:
                words = line.split()
                new_class.add_duration(int(words[2]))

            #Parse Lab
            elif 'lab' in line:
                words = line.split()
                if words[2] is 'true':
                    new_class.add_lab(True)
                else:
                    new_class.add_lab(False)

            #Parse Num Seats
            elif 'seats' in line:
                words = line.split()
                new_class.add_seats(int(words[2]))

            lines += 1
            line = file_list[lines]

        self.num_courses += 1
        return lines
        
    #Reads room data from config file, adds object to list
    def parse_room(self,file_list,lines,room_id):

        if self.room_list is None:
            self.room_list = []
            
        self.room_list.append(Room())
        room = self.room_list[len(self.room_list)-1]

        line = file_list[lines]

        while 'end' not in line:
            #Parse Name
            if 'name' in line:
                words = line.split()
                room.add_name(words[2])

            elif 'lab' in line:
                words = line.split()
                if 'true' in words[2]:
                    room.add_lab(True)
                else:
                    room.add_lab(False)

            elif 'size' in line:
                words = line.split()
                room.add_seats(int(words[2]))

            lines += 1
            line = file_list[lines]

        room.id = room_id
        self.num_rooms += 1
        return lines
