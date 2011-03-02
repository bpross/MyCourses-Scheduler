#!/usr/bin/python

"""
Employee Scheduler v0.1
Author: Benjamin Ross benr22@gmail.com
Date: 2/27

Shift Data Structure
"""

class Shift:

    def __init__(self, name = None, day = None, start_time = None,
                 end_time = None, num_employees = None, employee_list = None):
    """
    Constructor 
    @param name: name of the shift
    @param day: day of the shift
    @param start_time: start time of the shift
    @param end_time: end time of the shift
    @param num_employees: number of employees needed for the shift
    @param employee_list: list of employees schedule for this shift
    """

    if name is None:
        self.name = "Default"
    else:
        self.name = name

    if day is None:
        self.day = None
    else:
        self.day = day

    if start_time is None:
        self.start_time = 0
    else:
        self.start_time = start_time

    if end_time is None:
        self.end_time = 0
    else:
        self.end_time = end_time

    if num_employees is None:
        self.num_employees = 0
    else:
        self.num_employees = num_employees

    if employee_list is None:
        self.employee_list = None
    else:
        self.employee_list = employee_list


    def set_name(self, name):
    """
    Sets the name of the Shift
    """
   
    self.name = name

    def get_name(self):
    """
    Returns the name of the Shift
    """

    return self.name

    def set_day(self, day):
    """
    Sets the day of the shift
    Sunday is 0 Saturday is 7
    """

    self.day = day

    def get_day(self):
    """
    Returns the day of the shift
    """

    return self.day

    def set_start_time(self, start_time):
    """
    Sets the start time of the Shift
    """
    
    self.start_time = start_time

    def get_start_time(self):
    """
    Returns the start time of the shift
    """

    return self.start_time

    def set_end_time(self, end_time):
    """
    Sets the end time of the Shift
    """

    self.end_time = end_time

    def get_end_time(self):
    """
    Returns the end time of the Shift
    """

    return self.end_time

    def set_num_employees(self, num_employees):
    """
    Sets the number of employees for the Shift
    """

    self.num_employees = num_employees

    def get_num_employees(self):
    """
    Returns the number of employees for the Shift
    """

    return self.num_employees

    def set_employee_list(self, employee_list):
    """
    Sets the list of the employees scheduled
    """
 
    self.employee_list = employee_list

    def get_employee_list(self):
    """
    Returns the list of employees scheduled
    """

    return self.employee_list
