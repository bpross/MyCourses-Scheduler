"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import csv
from scheduler.algorithm import models
from scheduler.algorithm.models import *
from professor import Professor
from course_class import CourseClass
from room import Rooms
from course import Course
from datetime import date


class SimpleTest(TestCase):
    def test_basic_addition(self):
        file = open("/Users/esteggall/Scheduler/django/scheduler/administrator/testcsvfile.txt")
        testReader = csv.reader(file,delimiter = ' ', quotechar = '|')
        for row in testReader:
#            print row[0], row[1], row[2], row[3]
            if row[0] == "professor,":
                print row[0]
                print "professor"
                dept = Deptartment.objects.get(pk=row[5][0])
                if(dept == NULL):
                    print "No department yet"
                professor = Lecturer(idLecturer = row[1], Status = row[2], Name = row[3], Comment = row[4], idDeptartment = dept) 
                professor.save()
            elif row[0] == "building,":
                print row[0]
                print "building"
                building = Building(idBuilding = row[1][0], BldgName = row[2])               
                building.save()
            elif row[0] == "room,":
                print row[0]
                print "room"
                building = Building.objects.get(pk=row[1][0])
                if(building == NULL):
                    print "No Building yet"
                room = Room(idBuilding = building, idRoom = row[2], RoomNumber = row[3], Type = row[4], RoomName = row[5])
                room.save()
            elif row[0] == "course,":
                print row[0]
                print "course"
                dept = Department.objects.get(pk=row[2][0])
                if(dept == NULL):
                    print "No department yet"
                course = Class(idClass = row[1], idDepartment = dept, Class = row[3], ClassDescription = row[4])
                course.save()
            elif row[0] == "course_class,":
                print row[0]
                print "course_class"
            elif row[0] == "school,":
                print "School"
                s = School(idSchool = row[1][0], School = row[2])
                s.save()
            elif row[0] == "department,":
                print "Department"
                d = Department(idSchool = school, idDepartment = row[2], Department = row[3], DeptAbbrev = row[4])
                d.save()
            else:
                print "wrong place"

