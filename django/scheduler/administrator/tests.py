
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from csv_import import CSV
import os


class SimpleTest(TestCase):

	def test_basic_addition(self):
		DIRNAME = os.path.dirname(__file__)

        #csv_init = CSV()
        #csv_init.print_database() # Why is this invalid syntax?
        #csv_init.csv_import(os.path.join(DIRNAME, 'school.csv'), "school")
        #csv_init.csv_import(os.path.join(DIRNAME, 'department.csv', "department")
        #csv_init.csv_import(os.path.join(DIRNAME, 'building.csv', "building")
        #csv_init.csv_import(os.path.join(DIRNAME, 'professor.csv', "professor")
        #csv_init.csv_import(os.path.join(DIRNAME, 'room.csv', "room")
        #csv_init.csv_import(os.path.join(DIRNAME, 'course.csv', "course")
        #csv_init.csv_import(os.path.join(DIRNAME, 'course_class.csv', "course_class")
    
        #csv_init.print_database()