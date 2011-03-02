from django.utils import unittest
from algorithm.models import School, Department, Class, Prerequisite, Building, Room, Period, Lecturer, ClassInstance, ClassLab, Person, Role, PersonRole 
from algotest import Algorithm
from administrator.models import *
from datetime import date
import os # This is for creating paths to test files.

class test_AlgorithmTestCase(unittest.TestCase):

	def setUp(self):
		pass
	
	def tearDown(self):
		pass
	
	def test_saveData(self):
		# Create School in Database
		s = School(idSchool = 1, School = "UC Santa Cruz")
		# Save to Database
		s.save()
		d = Department(idSchool = s, idDepartment = 1, Department = "CompSci", DeptAbbrev = "CMPS") 
		d.save()
		c1 = Class(idClass = 1, idDepartment = d, Class = "CMPS 115", ClassDescription = "Kickin ass")
		c1.Lab = False 
		c1.SeatNum = 45
		c2 = Class(idClass = 2, idDepartment = d, Class = "CMPS 130", ClassDescription = "Meh")
		c2.Lab = False
		c2.SeatNum = 45
	
		c1.save()
		c2.save()
	
		b = Building(idBuilding = 1, BldgName = "BE")
	
		b.save()
	
	
		r1 = Room(idBuilding = b, idRoom = 1, RoomNumber = "BE105", Type = "Lab", RoomName = "Home")
		r2 = Room(idBuilding = b, idRoom = 2, RoomNumber = "BE104", Type = "Not Lab", RoomName = "HomeJr")
	
		r1.save()
		r2.save()
	
		l1 = Lecturer(idLecturer = 1, Status = "Active", Name = "Linda Werner", Comment = "Currently teaching CS115", idDepartment = d)
		l2 = Lecturer(idLecturer = 2, Status = "Active", Name = "Patrick Tantalo", Comment = "Not teaching", idDepartment = d)
	
		l1.save()
		l2.save()
	
		p1 = Period(idPeriod = 1, period = "first", StartDate = date.today(), EndDate = date.today(), InstructionBegins = date.today(), InstructionEnds = date.today())
		p2 = Period(idPeriod = 2, period = "Second", StartDate = date.today(), EndDate = date.today(), InstructionBegins = date.today(), InstructionEnds = date.today())
		p1.save()
		p2.save()
	
		cc1 = ClassInstance(idClass = c1, idClassInstance = 1, idPeriod = p1, ClassTime = "morning", Section = "Yes", idLecturer = l1, LecturerOfficeHours = "Afternoon", TAOfficeHours = "Night", idTA = 1, idBuilding = b, idRoom = r1)
		cc2 = ClassInstance(idClass = c2, idClassInstance = 2, idPeriod = p2, ClassTime = "morning", Section = "Yes", idLecturer = l2, LecturerOfficeHours = "Afternoon", TAOfficeHours = "Night", idTA = 1, idBuilding = b, idRoom = r2)
		
		cc1.save()
		cc2.save()

#        DIRNAME = os.path.dirname(__file__)
#        csv_init = CSV()
#        csv_init.print_database()
#        csv_init.csv_import("/Users/esteggall/Scheduler/django/administrator/school.csv"), "school")
#        csv_init.csv_import('/Users/esteggall/Scheduler/django/administrator/department.csv'), "department")
#        csv_init.csv_import('/Users/esteggall/Scheduler/django/administrator/professor.csv'), "professor")
#        csv_init.csv_import('/Users/esteggall/Scheduler/django/administrator/room.csv'), "room")
#        csv_init.csv_import('/Users/esteggall/Scheduler/django/administrator/course.csv'), "course")
#        csv_init.csv_import('/Users/esteggall/Scheduler/django/administrator/course_class.csv'), "course_class")
#        csv_init.print_database()

	def test_scheduler(self):
		Algorithm();
