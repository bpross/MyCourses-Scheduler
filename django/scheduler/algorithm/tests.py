from django.utils import unittest
from algorithm.models import School, Department, Class, Prerequisite, Building, Room, Period, Lecturer, ClassInstance, ClassLab, Person, Role, PersonRole 
from algotest import Algorithm

class test_AlgorithmTestCase(unittest.TestCase):

	def setUp(self):
		pass
	
	def tearDown(self):
		pass
	
	def test_saveData(self):
		print "Start Test"
		
		# This statement imports all of the fields from interface/models.py
		
		
		# Create School in Database
		s = School(idSchool = 1, School = "UC Santa Cruz")
		# Save to Database
		s.save()
		
		#Save to python variables
		name = s.School
		num = s.idSchool
		
		# Create department
		d = Department(idDepartment = 2, idSchool = s, Department = "CompSci", DeptAbbrev = "CMPS") 
		
		d.save()

		
		
		# Create class
		c = Class(idDepartment = d, idClass = 3, Class = "Software Engineering", ClassDescription = "Made to kickass")
		
		c.save()
		
		# Create prerequisites
		pre = Prerequisite(idPrereq = 4, ClassID = c)
		
		pre.save()
		
		
		#Create Building
		b = Building(idBuilding = 5, BldgName = "Baskin Engineering")
		
		#Save
		b.save()
				
		# Create Room
		r = Room(idBuilding = b, idRoom = 6, RoomNumber = "BE105", Type = "Comp Lab", RoomName = "Home")
		
		# Save to Database
		r.save()
		
		import datetime
		# Create Period in database
		p = Period(idPeriod = 7, period = "3rd", StartDate = datetime.datetime.now(), EndDate = datetime.datetime.now(), InstructionBegins = datetime.datetime.now(), InstructionEnds = datetime.datetime.now())
		
		# Save to database
		p.save()
		
		# Create Lecturer
		l = Lecturer(idLecturer = 8, Status = "Teaching", Name = "Linda Werner", Comment = "Works in San Jose on Tues/Thurs", idDepartment = d)
		
		l.save
		
		#Creates Class Instance
		ci = ClassInstance(idClass = c, idClassInstance = 10, idPeriod = p, ClassTime = "Noon", Section = "yes", idLecturer = l, LecturerOfficeHours = "Afternoon", TAOfficeHours = "Morning", idTA = 11, idBuilding = b, idRoom = r)
		
		ci.save()
		
		#Creates Class Lab
		cl = ClassLab(idClassInstance = ci, idClassLab = 12, LabName = "BE104", LabTime = "Noon", idRoom = r, idBuilding = b)
		
		cl.save()
		
		#Creates Person
		p = Person(idPerson = 14, FName = "Erik", MInitial = 'Q', LName = "Steggall", Suffix = "None", Prefix = "None")
		
		p.save()
		
		# Create Role 
		role = Role(idRole =15, Role = "Student")
		
		role.save()
		
		
		#Create Person Role
		pr = PersonRole(idPerson = p, idRole = role)
		
		pr.save()

	def test_scheduler(self):
		Algorithm();