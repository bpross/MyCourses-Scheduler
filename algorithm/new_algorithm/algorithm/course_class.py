#!/usr/bin/local/python
#Author: Benjamin Ross(bpross)

"""
CourseClass
"""

class CourseClass:

    def __init__(self,professor = None, course = None,
                 num_seats = None, requires_lab = None,
                 duration = None):

        if professor is None:
            self.professor = None
        else:
            self.professor = professor
        if course = None:
            self.course = None
        else:
            self.course = course
        if num_seats = None:
            self.num_seats = None
        else:
            self.num_seats = num_seats
        if requires_lab = None:
            self.requires_lab = None
        else:
            self.requires_lab = requires_lab
        if duration is None:
            self.duration = None
        else:
            self.duration = duration


    #Returns True if another class has the same professor
    def professor_overlap(self,course):
        if self.professor is course.professor:
            return True
        else:
            return False

    #Returns the Professor Teaching the Class
    def get_professor(self):
        return self.professor

    #Returns the Class being taught
    def get_course(self):
        return self.course

    #Returns the Number of Seats Required
    def get_room_size(self):
        return self.num_seats

    #Returns True if course needs lab
    def needs_lab(self):
        return self.requires_lab

    #Returns the duration of the class
    def get_duration(self):
        return self.duration
