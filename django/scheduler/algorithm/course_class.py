#!/usr/bin/local/python
#Author: Benjamin Ross(bpross)

"""
CourseClass
"""
from course import Course
from professor import Professor

class CourseClass:

    def __init__(self,professor = None, course = None,
                 num_seats = None, requires_lab = None,
                 duration = None, id = None):

        if professor is None:
            self.professor = None
        else:
            self.professor = professor
        if course is None:
            self.course = None
        else:
            self.course = course
        if num_seats is None:
            self.num_seats = None
        else:
            self.num_seats = num_seats
        if requires_lab is None:
            self.requires_lab = None
        else:
            self.requires_lab = requires_lab
        if duration is None:
            self.duration = None
        else:
            self.duration = duration
        if id is None:
            self.id = None
        else:
            self.id = course_classID


    #Returns True if another class has the same professor
    def professor_overlap(self,course):
        if self.professor is course.professor:
            return True
        else:
            return False

    #Returns the Professor Teaching the Class
    def get_professor(self):
        return self.professor
    #Returns the professor id
    def get_professor_id(self):
        return self.professor.id
    #Returns the course id
    def get_course_id(self):
        return self.course.id

    #Adds/changes Professor Teaching the Class
    def add_professor(self,professor):
        self.professor = professor
        
    #Returns the Class being taught
    def get_course(self):
        return self.course

    #Adds/changes class being taught
    def add_course(self, course):
        self.course = course
        
    #Returns the Number of Seats Required
    def get_room_size(self):
        return self.num_seats

    #Adds/changes the number of seats required
    def add_seats(self, num_seats):
        self.num_seats = num_seats
        
    #Returns True if course needs lab
    def needs_lab(self):
        return self.requires_lab

    #Adds/changes lab requirement
    def add_lab(self, requires_lab):
        self.requires_lab = requires_lab
        
    #Returns the duration of the class
    def get_duration(self):
        return self.duration

    #Adds/changes duration of the class
    def add_duration(self, duration):
        self.duration = duration

    #Returns the ID of the course_class
    def get_course_classid(self):
        return self.id

    def print_course_class(self):
        self.course.print_course()
        self.professor.print_professor()
