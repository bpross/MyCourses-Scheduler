
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
        testReader = csv.reader(file,delimiter = ',', quotechar = '|')
        for row in testReader:
            dept = Department.objects.get(pk=row[4])
            if(dept == NULL):
                print "No department yet"
            new_professor = Lecturer(idLecturer = row[0], Status = row[1],\
                                     Name = row[2], Comment = row[3],\
                                     idDeptartment = dept) 
            new_professor.save()

    def store_school(self, filename = None):
        testReader = csv.reader(file,delimiter = ',', quotechar = '|')
        for row in testReader:
             print row[0], row[1]
             new_school = school(idSchool = row[0], School = row[1]) 
             new_school.save()


    def store_room(self, filename = None):

        testReader = csv.reader(file,delimiter = ',', quotechar = '|')
        for row in testReader:
            building = Building.objects.get(pk=row[0])
            if(building == NULL):
                print "No Building yet"
            new_room = Room(idBuilding = building, idRoom = row[1],\
                            RoomNumber = row[2], Type = row[3],\
                            RoomName = row[5])
            new_room.save()

    def store_building(self, filename = None):
        testReader = csv.reader(file,delimiter = ',', quotechar = '|')
        for row in testReader:
            new_building = Building(idBuilding = row[0], BldgName = row[1])   
            new_building.save()

    def store_course(self, filename = None):
        testReader = csv.reader(file,delimiter = ',', quotechar = '|')
        for row in testReader:
            dept = Department.objects.get(pk=row[1])
            if(dept == NULL):
                print "No department yet"
            new_course = Class(idClass = row[0], idDepartment = dept,\
                               Class = row[2], ClassDescription = row[3])
            new_course.save()
    
    def store_department(self, filename = None):
        testReader = csv.reader(file,delimiter = ',', quotechar = '|')
        for row in testReader:
            school = School.objects.get(pk=row[0])
            new_department = Department(idSchool = school, \
                                        idDepartment = row[1],\
                                        Department = row[2], \
                                        DeptAbbrev = row[3])
            new_department.save()

    def store_course_class(self, filename = None):
        testReader = csv.reader(file,delimiter = ',', quotechar = '|')
        for row in testReader:
            Class = Class.objects.get(pk=row[0]);
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
        testReader = csv.reader(file,delimiter = ',', quotechar = '|')
        for row in testReader:
            new_period = Period(idPeriod = row[0], period = row[1], \
                                StartDate = row[2], EndDate = row[3], \
                                InstructionBegins = row[4], \
                                InstructionEnds = row[5])
            new_period.save()    

    def print_database(self):

        all_class_instance = ClassInstance.objects.all()
        for ClassInstance in all_class_instance:
            lecturer = ClassInstance.idLecturer
            course = ClassInstance.idClass
            print "Course Schedule(professor: %s Course: %s)" % (lecturer.Name, course.Class)

        all_lecturers = Lecturer.objects.all()
        for Lecturer in all_lecturers:
            print "Lecturer name: %s, Lecturer ID: %d" % (Lecturer.Name, Lecturer.idLecturer)

        all_rooms = Room.objects.all()
        for Room in all_rooms:
            print "Room: %s, Room ID: %d seats: %d" % (Room.RoomName, Room.idRoom, Room.SeatNum)

        all_courses = Class.objects.all()
        for Class in all_courses:
             print "Course: %s, Course ID: %d " % (Class.Class, Class.idClass)



#import csv

# The following example doesn't use chunks. We probably should.
# f is the file we got passed from the upload. It only exists in memory; we should NOT write it to disk.
#def csv_import(f):
#	dialect = csv.Sniffer().sniff(f.read(1024))
#	f.seek(0)
#	reader = csv.reader(f, dialect)
#	for row in reader:
#		
#		pass

	# Parse the imported CSV file here
	# Reference: http://docs.djangoproject.com/en/1.2/topics/http/file-uploads/
	# "chunks()"
