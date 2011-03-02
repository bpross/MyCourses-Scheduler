#!/usr/bin/python

"""
Employee Scheduler v 0.1
Author: Benjamin Ross benr22@gmail.com
Date: 2/27

Employee Data Structure
"""

class Employee:

    def __init__(self, id = None, first_name = None, last_name = None,
                 times_available = None, hours_available = None
                 hours_scheduled = None):
    """
    Constructor of the Employee Class
    @param: id: id number of the employee
    @param: first_name: first name of the employee
    @param: last_name: last name of the employee
    @param: times_available: list of day/times employee is available
    @param: hours_available: total hours employee is available 
    @param: hours_scheduled: total hours employee is scheduled
    """

    if id = None:
        self.id = 0
    else:
        self.id = id

    if first_name = None:
        self.first_name = "First"
    else:
        self.first_name = first_name

    if last_name = None:
        self.last_name = "Last"
    else:
       self.last_name = last_name

    if times_available = None:
       self.times_available = [0]*(7*12)
    else:
       self.times_available = times_available
    if hours_available = None:

       self.hours_available = 20
    else:
       self.hours_available = hours_available

    if hours_scheduled = None:
       self.hours_scheduled = 0
    else:
       self.hours_schedule = hours_scheduled


    def set_id(self, new_id):
    """
    Sets the id of the employee to id
    """
    
    self.id = new_id

    def get_id(self):
    """
    Returns the id of the employee
    """ 

    return self.id

    def set_first_name(self, first_name):
    """
    Sets the First Name of the Employee
    """

    self.first_name = first_name

    def get_first_name(self):
    """
    Returns the First Name of the Employee
    """

    return self.first_name

    def set_last_name(self, last_name):
    """
    Sets the Last Name of the Employee
    """

    self.last_name = last_name

    def get_last_name(self):
    """
    Returns the Last Name of the Employee
    """

    return self.last_name

    def set_times_avail(self, times_available):
    """
    Sets the times the employee is available
    """

    self.times_available = times_available

    def get_times_avail(self):
    """
    Returns the times the employee is available
    """

    return self.times_available

    def set_hours_avail(self, hours_avail):
    """
    Sets the hours the employee is available
    """

    self.hours_available = hours_available

    def get_hours_available(self):
    """
    Returns the hours the employee is available
    """

    return self.hours_available

    def set_hours_scheduled(self, hours_schedule):
    """
    Sets the hours the employee is scheduled
    """

    self.hours_schedule = hours_scheduled

    def get_hours_scheduled(self):
    """
    Returns the hours the employee is scheduled
    """

    return self.hours_scheduled
