
from django.test import TestCase
import csv
from scheduler.algorithm import models
from scheduler.algorithm.models import *
from professor import Professor
from course_class import CourseClass
from room import Rooms
from course import Course
from datetime import date

class CSV:

    def csv_import(self, filename = None, flag = None):
        if filename is None:
            print "Error: Need file to parse"
        else:
            file = open(filename, 'r')
        if flag is None:
            print "Error: File Type needs to be specified!"
        else:
            if flag is "professor":
                self.store_professor(file)
            elif flag is "department":
                self.store_department(file)
            elif flag is "school":
                self.store_school(file)
            elif flag is "building":
                self.store_building(file)
            elif flag is "room":
                self.store_room(file)
            elif flag is "course":
                self.store_course(file)
            elif flag is "course_class":
                self.store_course_class(file)
            elif flag is "period":
                self.store_period(file)
            else:
                print "wrong place"

    def store_professor(self, filename = None):
        testReader = csv.reader(filename,delimiter = ',', quotechar = '|')
        for row in testReader:
            department = Department.objects.get(pk=1)
            if(department == None):
                print "No department yet"
            new_professor = Lecturer(idLecturer = row[0], Status = row[1],\
                                     Name = row[2], Comment = row[3],\
                                     idDepartment = department) 
            new_professor.save()

    def store_school(self, filename = None):
        testReader = csv.reader(filename,delimiter = ',', quotechar = '|')
        for row in testReader:
             print row[0], row[1]
             new_school = School(idSchool = row[0], School = row[1]) 
             new_school.save()

    def store_room(self, filename = None):
        testReader = csv.reader(filename,delimiter = ',', quotechar = '|')
        for row in testReader:
            building = Building.objects.get(pk=row[0])
            if(building == None):
                print "No Building yet"
            new_room = Room(idBuilding = building, idRoom = row[1],\
                            RoomNumber = row[2], Type = row[3],\
                            RoomName = row[4])
            new_room.save()

    def store_building(self, filename = None):
        testReader = csv.reader(filename,delimiter = ',', quotechar = '|')
        for row in testReader:
            new_building = Building(idBuilding = row[0], BldgName = row[1])   
            new_building.save()

    def store_course(self, filename = None):
        testReader = csv.reader(filename,delimiter = ',', quotechar = '|')
        for row in testReader:
            department = Department.objects.get(pk=row[0])
            if(department == None):
                print "No department yet"
            new_course = Class(idClass = row[1], idDepartment = department,\
                               Class = row[2], ClassDescription = row[3])
            new_course.save()

    def store_department(self, filename = None):
        testReader = csv.reader(filename,delimiter = ',', quotechar = '|')
        for row in testReader:
            school = School.objects.get(pk=row[0])
            new_department = Department(idSchool = school, \
                                        idDepartment = row[1],\
                                        Department = row[2], \
                                        DeptAbbrev = row[3])
            new_department.save()

    def store_course_class(self, filename = None):
        testReader = csv.reader(filename,delimiter = ',', quotechar = '|')
        for row in testReader:
            Class = Class.objects.get(pk=row[0]);
            if(course == None):
                print "No class"
            period = Period.objects.get(pk=row[2])
            if(period == None):
                print "No period"
            professor = Lecturer.objects.get(pk=row[5])
            if(professor == None):
                print "No professor"
            building = Building.objects.get(pk=row[8])
            if(building == None):
                print "No building yet"
            room = Room.objects.get(pk=row[9])
            if(building == None):
                print "No room"
            new_course_class = ClassInstance(idClass = course, \
                                             idClassInstance = row[1], \
                                             idPeriod = period, \
                                             ClassTime = row[3], \
                                             Section = row[4], \
                                             idLecturer = professor,\
                                             TAOfficeHours = row[6],\
                                             idTA = row[7],\
                                             idBuilding = building,\
                                             idRoom = room)  
            new_course_class.save()

    def store_period(self, filename = None):
        testReader = csv.reader(filename,delimiter = ',', quotechar = '|')
        for row in testReader:
            new_period = Period(idPeriod = row[0], period = row[1], \
                                StartDate = row[2], EndDate = row[3], \
                                InstructionBegins = row[4], \
                                InstructionEnds = row[5])
            new_period.save()    

    def print_database(self):
        from scheduler.algorithm import models
        from scheduler.algorithm.models import *
        print "                         Contents of Database "
        all_schools = School.objects.all()
        if(all_schools !=None):
            for School in all_schools:
                print "School: %s, School ID: %d " % (School.School, School.idSchool)

        all_departments = Department.objects.all()
        if(all_departments != None):
            for Department in all_departments:
                print "Department: %s, Department ID: %d " % (Department.Department, Department.idDepartment)

        all_buildings = Building.objects.all()
        if(all_buildings != None):
            for Building in all_buildings:
                print "Building: %s, Building ID: %d " % (Building.BldgName, Building.idBuilding)
        all_class_instance = ClassInstance.objects.all()
        if (all_class_instance != None):
            for ClassInstance in all_class_instance:
                lecturer = ClassInstance.idLecturer
                course = ClassInstance.idClass
                print "Course Schedule(professor: %s Course: %s)" % (lecturer.Name, course.Class)

        all_lecturers = Lecturer.objects.all()
        if (all_lecturers != None):
            for Lecturer in all_lecturers:
                print "Lecturer name: %s, Lecturer ID: %d" % (Lecturer.Name, Lecturer.idLecturer)

        all_rooms = Room.objects.all()
        if (all_rooms != None):
            for Room in all_rooms:
                print "Room: %s, Room ID: %d seats: %d" % (Room.RoomName, Room.idRoom, Room.SeatNum)

        all_courses = Class.objects.all()
        if (all_courses != None):
            for Class in all_courses:
                print "Course: %s, Course ID: %d " % (Class.Class, Class.idClass)
