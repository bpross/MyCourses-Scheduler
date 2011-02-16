
print "Start Test"
# Hopefully this will work
# This statement imports all of the fields from interface/models.py
from scheduler.administrator.csv_import import CSV
from algorithm.models import School, Department, Class, Prerequisite, Building, Room, Period, Lecturer, ClassInstance, ClassLab, Person, Role, PersonRole 
from professor import Professor
from course_class import CourseClass
from room import Rooms
from course import Course
from configuration import Configuration
from algo_config import Config
from datetime import date
from schedule import Schedule

def Algorithm():


################################
#   call to database config    #
################################

    configuration = Config()
    course_list = configuration.get_course_list()
    room_list = configuration.get_room_list()
    prof_list = configuration.get_prof_list()
    course_class_list = configuration.get_course_class_list()

################################
#   call to origional config   #
################################
   

#    config = Configuration()
#    course_list = config.


################################
#   scheduler called here      #
################################
#   From schedule_test.py      #
################################

    configuration.print_database()
    test_schedule = Schedule(None, configuration)
    test_schedule.algorithm()
    test_schedule.print_chromosomes()
    print "              This what is in the Database"
    configuration.print_database()
    test_float = test_schedule.get_overall_fitness()
    print test_float
    print "End Test"