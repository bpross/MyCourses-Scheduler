
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
    d.save()
    c1 = Class(idClass = 1, idDepartment = d, Class = "CMPS 115", ClassDescription = "Kickin ass")
    c1.Lab = False 
    c1.SeatNum = 45
    c2 = Class(idClass = 2, idDepartment = d, Class = "CMPS 130", ClassDescription = "Sucks")
    c2.Lab = False
    c2.SeatNum = 45

    c1.save()
    c2.save()

    b = Building(idBuilding = 1, BldgName = "BE")

    b.save()


    r1 = Room(idBuilding = b, idRoom = 1, RoomNumber = "BE105", Type = "Lab", RoomName = "Home")
    r2 = Room(idBuilding = b, idRoom = 2, RoomNumber = "BE104", Type = "Not Lab", RoomName = "HELL")

    r1.save()
    r2.save()

    l1 = Lecturer(idLecturer = 1, Status = "Active", Name = "Linda Werner", Comment = "Good Teacher", idDepartment = d)
    l2 = Lecturer(idLecturer = 2, Status = "Active", Name = "Van Guelder", Comment = "Is a douche", idDepartment = d)

    l1.save()
    l2.save()

#######          This is what we'll need               ##############
    def __init__(self,prof_list = None, course_list = None,
                 room_list = None, classes_list = None):
        if prof_list is None:
            self.prof_list = None
        else:
            self.prof_list = prof_list
        if course_list is None:
            self.course_list = None
        else:
            self.course_list = course_list
        if room_list is None:
            self.room_list = None
        else:
            self.room_list = room_list
        if classes_list is None:
            self.classes_list = None
        else:
            self.classes_list = classes_list

        self.empty = True
        self.num_professors = 0
        self.num_rooms = 0
        self.num_classes = 0
        self.num_courses = 0


    def is_empty(self, Class):
        return self.empty


# This section takes values from the database and stores them in course list 
    
    print "This will print out all the courses currently in the database"

    course_list = []
    all_courses = Class.objects.all()
    
    for Class in all_courses:
#       print "Course = %s Course ID = %d" % (Class.Class, Class.idClass)
       new_course = Course()
       new_course.id = Class.idClass
       new_course.name = Class.Class
#       new_course.print_course()
       #if course_list is None:
       #   course_list = []
       course_list.append(new_course)

    for Course in course_list:
        Course.print_course()
# This section takes values from the database and stores them in room list 
    room_list = []
    all_rooms = Room.objects.all()
      
    print "This will print out all of the Rooms currently in the database"
 
    for Room in all_rooms:
        print "Room = %s, Room ID = %d seats = %d" % (Room.RoomName, Room.idRoom, Room.SeatNum)
        new_room = Rooms()
        new_room.seat_num = Room.SeatNum
        new_room.lab = Room.Lab
        new_room.name = Room.RoomName
        room_list.append(new_room)

#    for Rooms in room_list:
#        Rooms.print_room()

# This section takes values from the database and stores them in room list 
    
    print "This will print out all of the professors currently in the database"
    prof_list = []

    all_lecturers = Lecturer.objects.all()
    
    for Lecturer in all_lecturers:
        print "Lecturer name = %s, Lecturer ID = %d" % (Lecturer.Name, Lecturer.idLecturer)
        new_prof = Professor()
        new_prof.name = Lecturer.Name
        new_prof.id = Lecturer.idLecturer
        new_prof.course_list = course_list

    for Professor in prof_list:
        Professor.print_professor()

    
    print "End Test"
