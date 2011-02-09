
print "Start Test"
# Hopefully this will work
# This statement imports all of the fields from interface/models.py
from algorithm.models import School, Department, Class, Prerequisite, Building, Room, Period, Lecturer, ClassInstance, ClassLab, Person, Role, PersonRole 
from professor import Professor
from course_class import CourseClass
from room import Rooms
from course import Course
from configuration import Configuration
from algo_config import Config
from datetime import date
class Algorithm():
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
    configuration = Config()

    course_list = configuration.get_course_list()

    room_list = configuration.get_room_list()

    prof_list = configuration.get_prof_list()

    course_class_list = configuration.get_course_class_list()


#From schedule_test.py

    from schedule import Schedule

#    test_schedule = Schedule(None, configuration)

#    test_schedule.algorithm()

#    test_schedule.print_chromosomes()

#    test_float = test_schedule.get_overall_fitness()

#    print test_float

print "End Test"
