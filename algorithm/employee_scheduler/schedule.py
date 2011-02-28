#!/usr/bin/python

"""
Employee Scheduler v 0.1
Author: Benjamin Ross benr22@gmail.com
Date: 2/27

Scheduler Class
"""
from employee import Employee
from shift import Shift
import random

class Chromosome:

    def __init__(self, shift = None):
        """
        Constructor
        @param shift: shift being scheduled
        """
 
        if shift is None:
            self.shift = None
        else:
            self.shift = shift

        self.fitness = 0   

class Schedule:

    def __init__(self, shifts = None, employees = None):
        """
        Constructor
        @param shifts: list of shifts to schedule
        @param employees: list of employees
        """

        if shifts is None:
            self.shifts = None
        else:
            self.shifts = shifts

        if employees is None:
            self.employees = None
        else:
            self.employees = employees

        self.chromo_list = None

    def set_shifts(self, shifts):
        """
        Sets the shifts
        """

        self.shifts = shifts

    def get_shifts(self):
        """
        Returns the shifts
        """

        return self.shifts

    def set_employees(self, employees):
        """
        Sets the employees
        """
  
        self.employees = employees

    def init_schedule(self):
        """
        Initalizes the shifts with random employees
        """

        self.chromo_list = [Chromosome] * len(self.shifts.size)
 
        while iter is not len(self.chromo_list.size):
            self.chromo_list[iter].shift = self.shifts[iter]

        
