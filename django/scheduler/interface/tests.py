"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

#from django.test import TestCase

#class SimpleTest(TestCase):
#    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
#        self.failUnlessEqual(1 + 1, 2)

#__test__ = {"doctest": """
#Another way to test that 1 + 1 is equal to 2.

#>>> 1 + 1 == 2
#True
#"""}



"""
Models test


from django.utils import unittest
from models import School

class SchoolTestCase(unittest.TestCase):
    def setUp(self):
        self.UCSC = School.objects.create(SchoolName="UCSC", idSchool="1234")

    def testSpeaking(self):
	self.assertEqual(self.UCSC.speak(), 'The slug says "hi" ')

"""
