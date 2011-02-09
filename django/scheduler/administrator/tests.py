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
        testReader = csv.reader(file,delimiter = ',', quotechar = '|')
        for row in testReader:
            if row[0] == "professor":
                
            elif row[0] == "department":
            elif row[0] == "school":
            elif row[0] == "building":
            elif row[0] == "room":
            elif row[0] == "course":
            elif row[0] == "course_class":
            elif row[0] == "period":
            else:
                print "wrong place"
           


    def store_professor(self, filename = None):
        print "in professor"
        file = open("/Users/esteggall/Scheduler/django/scheduler/administrator/"+ filename)
        testReader = csv.reader(file,delimiter = ',', quotechar = '|')
        for row in testReader:
            dept = Department.objects.get(pk=row[4])
            if(dept == NULL):
                print "No department yet"
            new_professor = Lecturer(idLecturer = row[0], Status = row[1], Name = row[2], Comment = row[3], idDeptartment = dept) 
            new_professor.save()

    def store_school(self, filename = None):
        print "in school"
        file = open("/Users/esteggall/Scheduler/django/scheduler/administrator/"+ filename)
        testReader = csv.reader(file,delimiter = ',', quotechar = '|')
        for row in testReader:
             print row[0], row[1]
             new_school = school(idSchool = row[0], School = row[1]) 
             new_school.save()

    def store_room(self, filename = None):
        print "in room"
        file = open("/Users/esteggall/Scheduler/django/scheduler/administrator/"+ filename)
        testReader = csv.reader(file,delimiter = ',', quotechar = '|')
        for row in testReader:
            building = Building.objects.get(pk=row[0])
            if(building == NULL):
                print "No Building yet"
            new_room = Room(idBuilding = building, idRoom = row[1], RoomNumber = row[2], Type = row[3], RoomName = row[5])
            new_room.save()
        
    def store_building(self, filename = None):
        print "in building"
        file = open("/Users/esteggall/Scheduler/django/scheduler/administrator/"+ filename)
        testReader = csv.reader(file,delimiter = ',', quotechar = '|')
        for row in testReader:
            new_building = Building(idBuilding = row[0], BldgName = row[1])               
            new_building.save()

    def store_course(self, filename = None):
        print "in course"
        file = open("/Users/esteggall/Scheduler/django/scheduler/administrator/"+ filename)
        testReader = csv.reader(file,delimiter = ',', quotechar = '|')
        for row in testReader:
            dept = Department.objects.get(pk=row[1])
            if(dept == NULL):
                print "No department yet"
            new_course = Class(idClass = row[0], idDepartment = dept, Class = row[2], ClassDescription = row[3])
            new_course.save()
    
    def store_department(self, filename = None):
        print "in department"
        file = open("/Users/esteggall/Scheduler/django/scheduler/administrator/"+ filename)
        testReader = csv.reader(file,delimiter = ',', quotechar = '|')
        for row in testReader:
            school = School.objects.get(pk=row[0])
            new_department = Department(idSchool = school, idDepartment = row[1], Department = row[2], DeptAbbrev = row[3])
            new_department.save()

    def store_course_class(self, filename = None):
        print "in course_class"
        file = open("/Users/esteggall/Scheduler/django/scheduler/administrator/"+ filename)
        testReader = csv.reader(file,delimiter = ',', quotechar = '|')
        for row in testReader:
            course = Class.objects.get(pk=row[0];
            if(course == NULL):
                print "No class"
            period = Period.objects.get(pk=row[2])
            if(period == NULL):
                print "No period"
            professor = Lecturer.objects.get(pk=row[5])
            if(professor == NULL):
                print "No professor"
            building = Building.objects.get(pk=row[8])
            if(building == NULL):
                print "No building yet"
            room = Room.objects.get(pk=row[9])
            if(building == NULL):
                print "No room"
            new_course_class = ClassInstance(idClass = course, idClassInstance = row[1], idPeriod = period, ClassTime = row[3], Section = row[4], idLecturer = professor, TAOfficeHours = row[6], idTA = row[7], idBuilding = building, idRoom = room)  
            new_course_class.save()


    def store_period(self, filename = None):
        print "in period"
        file = open("/Users/esteggall/Scheduler/django/scheduler/administrator/"+ filename)
        testReader = csv.reader(file,delimiter = ',', quotechar = '|')
        for row in testReader:
            new_period = Period(idPeriod = row[0], period = row[1], StartDate = row[2], EndDate = row[3], InstructionBegins = row[4], InstructionEnds = row[5])
            new_period.save()    

            
                 
           


"""
        file = open("/Users/esteggall/Scheduler/django/scheduler/administrator/testcsvfile.txt")
        testReader = csv.reader(file,delimiter = ',', quotechar = '|')
        for row in testReader:
#            print row[0], row[1], row[2], row[3]
            if row[0] == "professor":
                print row[0]
                print "professor"
                dept = Deptartment.objects.get(pk=row[5])
                if(dept == NULL):
                    print "No department yet"
                professor = Lecturer(idLecturer = row[1], Status = row[2], Name = row[3], Comment = row[4], idDeptartment = dept) 
                professor.save()
            elif row[0] == "building":
                print row[0]
                print "building"
                building = Building(idBuilding = row[1], BldgName = row[2])               
                building.save()
            elif row[0] == "room":
                print row[0]
                print "room"
                building = Building.objects.get(pk=row[1])
                if(building == NULL):
                    print "No Building yet"
                room = Room(idBuilding = building, idRoom = row[2], RoomNumber = row[3], Type = row[4], RoomName = row[5])
                room.save()
            elif row[0] == "course":
                print row[0]
                print "course"
                dept = Department.objects.get(pk=row[2])
                if(dept == NULL):
                    print "No department yet"
                course = Class(idClass = row[1], idDepartment = dept, Class = row[3], ClassDescription = row[4])
                course.save()
            elif row[0] == "course_class":
                print row[0]
                print "course_class"
            elif row[0] == "school":
                print "School"
                school = School(idSchool = row[1], School = row[2])
                school.save()
            elif row[0] == "department":
                print "Department"
                d = Department(idSchool = school, idDepartment = row[2], Department = row[3], DeptAbbrev = row[4])
                d.save()
            else:
                print "wrong place"
"""
