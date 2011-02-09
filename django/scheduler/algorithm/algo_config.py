# Hopefully this will work
# This statement imports all of the fields from interface/models.py
from algorithm.models import School, Department, Class, Prerequisite, Building, Room, Period, Lecturer, ClassInstance, ClassLab, Person, Role, PersonRole 
from professor import Professor
from course_class import CourseClass
from room import Rooms
from course import Course

class Config:
    
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
    #Returns the professor with specified ID
    #If there is no professor with such ID method returns False
    def get_professor_by_id(self,id):

        for professor in self.prof_list:
            new_id = professor.get_id()
            if new_id is id:
                return professor

        #Not in list
        return None

    #Returns the number of parsed professors
    def get_num_prof(self):
        return self.num_professors

    #Returns the course with specified ID
    #If there is no course with such ID method returns False
    def get_course_by_id(self, id):

        for course in self.course_list:
            new_id = course.get_id()
            if new_id is id:
                return course

        #Not in list
        return False

    #Returns the number of parses courses
    def get_num_course(self):
        return self.num_courses

    #Returns the room with specified id
    #If there is no room with such ID method returns False
    def get_room_by_id(self, id):

        for room in self.room_list:
            new_id = room.get_id()
            if new_id is id:
                return room

        #Not in List
        return None

    #Returns the number of parsed rooms
    def get_num_rooms(self):
        return self.num_rooms

    #Returns the class with specified course
    #IF there is no class with such ID method returns False
    def get_class_by_course(self,course_id):

        for new_class in self.classes_list:
            new_course = new_class.get_course()
            
            if new_course is course_id:
                return new_class

        #Not in list
        return False

    #Returns the number of parsed classes
    def get_num_classes(self):
        return self.num_classes

###### parse_file
    def get_data(self):
        self.get_course_list()
        self.get_prof_list()
        self.get_room_list()
        self.get_course_class_list()




    # This section takes values from the database and stores them in course list 
    def get_course_list(self):
        from algorithm.models import School, Department, Class, Prerequisite, Building, Room, Period, Lecturer, ClassInstance, ClassLab, Person, Role, PersonRole 
        from course import Course
        print "This will print out all the courses currently in the database"
    
        self.course_list = []
        all_courses = Class.objects.all()
        
        for Class in all_courses:
           new_course = Course()
           new_course.id = Class.idClass
           new_course.name = Class.Class
           self.course_list.append(new_course)
           self.num_courses += 1

        for Course in self.course_list:
            Course.print_course()

    # This section takes values from the database and stores them in room list 
    def get_room_list(self):
        from algorithm.models import School, Department, Class, Prerequisite, Building, Room, Period, Lecturer, ClassInstance, ClassLab, Person, Role, PersonRole 
        from room import Rooms
        self.room_list = []
        all_rooms = Room.objects.all()
        print "This will print out all of the Rooms currently in the database"
    
        for Room in all_rooms:
            print "Room = %s, Room ID = %d seats = %d" % (Room.RoomName, Room.idRoom, Room.SeatNum)
            new_room = Rooms()
            new_room.seat_num = Room.SeatNum
            new_room.lab = Room.Lab
            new_room.name = Room.RoomName
            new_room.id = Room.idRoom
            self.room_list.append(new_room)
            self.num_rooms += 1

        for Rooms in self.room_list:
            Rooms.print_room()
    
    # This section takes values from the database and stores them in room list 
    def get_prof_list(self):
        from algorithm.models import School, Department, Class, Prerequisite, Building, Room, Period, Lecturer, ClassInstance, ClassLab, Person, Role, PersonRole 
        from professor import Professor
        
        print "This will print out all of the professors currently in the database"
        self.prof_list = []
    
        all_lecturers = Lecturer.objects.all()
        
        for Lecturer in all_lecturers:
            print "Lecturer name = %s, Lecturer ID = %d" % (Lecturer.Name, Lecturer.idLecturer)
            new_prof = Professor()
            new_prof.name = Lecturer.Name
            new_prof.id = Lecturer.idLecturer
#            new_prof.course_list = course_list
            self.prof_list.append(new_prof)
            self.num_professors += 1

        for Professor in self.prof_list:
            Professor.print_professor()
   
    def get_course_class_list(self):        
        from algorithm.models import School, Department, Class, Prerequisite, Building, Room, Period, Lecturer, ClassInstance, ClassLab, Person, Role, PersonRole 
        from course_class import CourseClass
    # This section takes values from the database and stores them in course clas list 
        print "This will print out all of the course classes currently in the database"
        self.classes_list = []

        all_course_class = ClassInstance.objects.all()
        for ClassInstance in all_course_class:       

            new_prof = ClassInstance.idLecturer
            new_course = ClassInstance.idClass


            new_course_class = CourseClass()
            new_course_class.professor = new_prof.Name
            new_course_class.course = new_course.Class
            new_course_class.duration = 1
            new_course_class.lab = False
            self.classes_list.append(new_course_class)
            self.num_classes += 1

        for course_class in self.classes_list:
            print "(Professer: %s Course: %s Durration: %d Lab: %d)" % (course_class.professor, course_class.course, course_class.duration, course_class.lab)
        
