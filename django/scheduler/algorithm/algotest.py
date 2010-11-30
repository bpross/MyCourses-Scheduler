print "Start Test"
# Hopefully this will work
# This statement imports all of the fields from interface/models.py
from algorithm.models import School, Department, Class, Prerequisite, Building, Room, Period, Lecturer, ClassInstance, ClassLab, Person, Role, PersonRole 

class Algorithm():
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

    print "End Test"
