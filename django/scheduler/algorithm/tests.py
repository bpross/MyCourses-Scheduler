from django.utils import unittest
from algorithm.models import School, Department, Class, Prerequisite, Building, Room, Period, Lecturer, ClassInstance, ClassLab, Person, Role, PersonRole 

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
		# print out values from database
		print "School:\nSchool ID = %d, School name = %s" % (s.idSchool, s.School)
		
		#Save to python variables
		name = s.School
		num = s.idSchool
		#print out python values of school
		print "Name = %s, Num = %d" % (name, num)
		
		# Create department
		d = Department(idDepartment = 2, idSchool = s, Department = "CompSci", DeptAbbrev = "CMPS") 
		
		d.save()
		
		# print out values
		print "Department:\nDepartment ID = %d, School id = %s, Department = %s Department Abbrev = %s" % (d.idDepartment, d.idSchool, d.Department, d.DeptAbbrev)
		
		
		# Create class
		c = Class(idDepartment = d, idClass = 3, Class = "Software Engineering", ClassDescription = "Made to kickass")
		
		c.save()
		
		# print out values
		print "Class:\nDept = %s, Class = %s, Class = %s, Class Description = %s" % (c.idDepartment, c.idClass, c.Class, c.ClassDescription)
		
		# Create prerequisites
		pre = Prerequisite(idPrereq = 4, ClassID = c)
		
		pre.save()
		
		# print out values
		print "Prerequisite:\nPrereq ID = %d, Class = %s" % (pre.idPrereq, pre.ClassID)
		
		#Create Building
		b = Building(idBuilding = 5, BldgName = "Baskin Engineering")
		
		#Save
		b.save()
		
		# print out values
		print "Building:\nBuilding = %s, BuildingID = %d" % (b.BldgName, b.idBuilding)
		
		# Create Room
		r = Room(idBuilding = b, idRoom = 6, RoomNumber = "BE105", Type = "Comp Lab", RoomName = "Home")
		
		# Save to Database
		r.save()
		
		# print out values from database
		print "Room:\nRoomID = %d, Building = %s, RoomNumber = %s, Type = %s, Roomname = %s" % (r.idRoom, r.idBuilding, r. RoomNumber, r.Type, r.RoomName)
		
		import datetime
		# Create Period in database
		p = Period(idPeriod = 7, period = "3rd", StartDate = datetime.datetime.now(), EndDate = datetime.datetime.now(), InstructionBegins = datetime.datetime.now(), InstructionEnds = datetime.datetime.now())
		
		# Save to database
		p.save()
		
		# Print out values from database
		print "Period:\nPeriod ID = %d, Period = %s, Start = %s, End = %s, Begining = %s, last day = %s" % (p.idPeriod, p.period, p.StartDate, p.EndDate, p.InstructionBegins, p.InstructionEnds)
		
		# Create Lecturer
		l = Lecturer(idLecturer = 8, Status = "Teaching", Name = "Linda Werner", Comment = "Works in San Jose on Tues/Thurs", idDepartment = d)
		
		l.save
		
		# Prints out values of Lecturer
		print "Lecturer:\nLecturer ID = %d, Status = %s, Name = %s, Comment = %s, Dept = %s" % (l.idLecturer, l.Status, l.Name, l.Comment, l.idDepartment)
		
		
		#Creates Class Instance
		ci = ClassInstance(idClass = c, idClassInstance = 10, idPeriod = p, ClassTime = "Noon", Section = "yes", idLecturer = l, LecturerOfficeHours = "Afternoon", TAOfficeHours = "Morning", idTA = 11, idBuilding = b, idRoom = r)
		
		ci.save()
		
		#print out valeus of Class instance
		print "Class Instance:\n Class = %s, Class Instance = %d, Period = %s, Time = %s, Section = %s, Lecturer = %s, Lecturer Office Hours = %s, TA office hours = %s, TA = %d, Building = %s, Room = %s" % (ci.idClass, ci.idClassInstance, ci.idPeriod, ci.ClassTime, ci.Section, ci.idLecturer, ci.LecturerOfficeHours, ci.TAOfficeHours, ci.idTA, ci.idBuilding, ci.idRoom)
		
		#Creates Class Lab
		cl = ClassLab(idClassInstance = ci, idClassLab = 12, LabName = "BE104", LabTime = "Noon", idRoom = r, idBuilding = b)
		
		cl.save()
		
		print "Class Lab:\nClass Instance = %s, Class Lab ID = %d, Lab name = %s, Lab time = %s, Room = %s, Building = %s" % (cl.idClassInstance, cl.idClassLab, cl.LabName, cl.LabTime, cl.idRoom, cl.idBuilding)
		
		#Creates Person
		p = Person(idPerson = 14, FName = "Erik", MInitial = 'Q', LName = "Steggall", Suffix = "None", Prefix = "None")
		
		p.save()
		
		print "Person:\nPerson = %d, name = %s %s %c %s %s)" % (p.idPerson, p.Prefix, p.FName, p.MInitial, p.LName, p.Suffix)
		
		# Create Role 
		role = Role(idRole =15, Role = "Student")
		
		role.save()
		
		print "Role:\n ID = %d, Role = %s" % (role.idRole, role.Role)
		
		
		#Create Person Role
		pr = PersonRole(idPerson = p, idRole = role)
		
		pr.save()
		
		print "Person Role:\nPerson = %s, Role = %s" % (pr.idPerson, pr.idRole)
