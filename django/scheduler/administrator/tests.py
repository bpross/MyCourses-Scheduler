
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from csv_import import CSV
import os


class SimpleTest(TestCase):

	def test_basic_addition(self):
		DIRNAME = os.path.dirname(__file__)

        csv_init = CSV()
        csv_init.print_database() # Why is this invalid syntax?
        csv_init.csv_import(os.path.join(DIRNAME, 'school.csv'), "school")
        csv_init.csv_import(os.path.join(DIRNAME, 'department.csv', "department")
        csv_init.csv_import(os.path.join(DIRNAME, 'building.csv', "building")
        csv_init.csv_import(os.path.join(DIRNAME, 'professor.csv', "professor")
        csv_init.csv_import(os.path.join(DIRNAME, 'room.csv', "room")
        csv_init.csv_import(os.path.join(DIRNAME, 'course.csv', "course")
        csv_init.csv_import(os.path.join(DIRNAME, 'course_class.csv', "course_class")
    
        csv_init.print_database()



"""
        if filename is None:
            print "Error: Need file to parse"
        else:
            file = open(filename)
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
"""  
