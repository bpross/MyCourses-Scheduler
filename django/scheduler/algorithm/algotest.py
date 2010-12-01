
print "Start Test"
# Hopefully this will work
# This statement imports all of the fields from interface/models.py
from algorithm.models import School, Department, Class, Prerequisite, Building, Room, Period, Lecturer, ClassInstance, ClassLab, Person, Role, PersonRole 
from professor import Professor
from course_class import CourseClass
from room import Rooms
from course import Course
from configuration import Configuration

class Algorithm():
    # Create School in Database
    s = School(idSchool = 1, School = "UC Santa Cruz")
    # Save to Database
    s.save()




    d = Department(idSchool = s, idDepartment = 1, Department = "CompSci", DeptAbbrev = "CMPS") 

    c1 = Class(idClass = 1, idDepartment = d, Class = "CMPS 115", ClassDescription = "Kickin ass")

    c2 = Class(idClass = 2, idDepartment = d, Class = "CMPS 130", ClassDescription = "Sucks")

    c1.save()
    c2.save()

    b = Building(idBuilding = 1, BldgName = "BE")


    r1 = Room(idBuilding = b, idRoom = 1, RoomNumber = "BE105", Type = "Lab", RoomName = "Home")
    r2 = Room(idBuilding = b, idRoom = 2, RoomNumber = "BE104", Type = "Not Lab", RoomName = "HELL")

    r1.save()
    r2.save()

    l1 = Lecturer(idLecturer = 1, Status = "Active", Name = "Linda Werner", Comment = "Good Teacher", idDepartment = d)
    l2 = Lecturer(idLecturer = 2, Status = "Active", Name = "Van Guelder", Comment = "Is a douche", idDepartment = d)

    l1.save()
    l2.save()

#######          This is what we'll need               ##############
    all_courses = Class.objects.all()

    print "This will print out all the courses currently in the database"

    for Class in all_courses:
       print "Course = %s Course ID = %d" % (Class.Class, Class.idClass)
       #new_course = Course()
       #new_course.id = Class.idClass
       #new_course.name = Class.Class
       #if course_list is None:
       #   self.course_list = []
       #self.course_list.append(new_course)

    all_rooms = Room.objects.all()
  
    print "This will print out all of the Rooms currently in the database"

    for Room in all_rooms:
        print "Room = %s, Room ID = %d" % (Room.RoomName, Room.idRoom)


    print "This will print out all of the Rooms currently in the database"

    all_lecturers = Lecturer.objects.all()

    for Lecturer in all_lecturers:
        print "Lecturer name = %s, Lecturer ID = %d" % (Lecturer.Name, Lecturer.idLecturer)




    print "End Test"
