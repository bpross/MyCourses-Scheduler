if __name__ == '__main__':
    import csv
    from django.scheduler.algorithm import models
    from professor import Professor
    from course_class import CourseClass
    from room import Rooms
    from course import Course
    from datetime import date

    file = open("/Users/esteggall/Scheduler/django/scheduler/administrator/testcsvfile.txt")
    testReader = csv.reader(file,delimiter = ' ', quotechar = '|')
    for row in testReader:
        print row[0], row[1], row[2], row[3]
        if row[0] == "professor,":
            print "professor"
        elif row[0] == "room,":
            print "room"
            new_room = Room(idBuilding = 1, idRoom = 1, RoomNumber = "BE105", Type = "Lab", RoomName = "CSlab")
        elif row[0] == "course,":
            print "course"
        elif row[0] == "course_class,":
            print "course_class"
        else:
            print "wrong place"


























"""
        if row[0] == "professor,":
            print "professor"
            print row[1]
            print row[2]
            print row[3]
        elif row[0] == "course":
            print "course"
            print row[1]
            print row[2]
            print row[3]
        elif row[0] == "room":
            print "room"
            print row[1]
            print row[2]
            print row[3]
        elif row[0] == "course_class":
            print "course_class"
            print row[1]
            print row[2]
            print row[3]
        else:
            print "Wrong Place"
            print row[0]
            print row[1]
            print row[2]
            print row[3]
"""            
