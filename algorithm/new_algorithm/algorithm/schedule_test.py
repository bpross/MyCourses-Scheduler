#!/usr/bin/python

#Author: Benjamin Ross
#Date: 11/29

"""
This tests the schedule module
"""

from schedule import Schedule

test_schedule = Schedule()

#test_schedule.get_config()

#print test_schedule.config.is_empty()

#test_schedule.init_chromosomes()

#test_schedule.print_chromosomes()

#test_float = test_schedule.get_overall_fitness()

#print test_float

#test_schedule.perform_crossover(1,10)

#test_schedule.print_chromosomes()

#test_float = test_schedule.get_overall_fitness()

#print test_float

#test_schedule.mutation_size = 5

#test_schedule.perform_mutations()

#test_schedule.print_chromosomes()

#test_float = test_schedule.get_overall_fitness()

#print test_float

test_schedule.algorithm()

test_schedule.print_chromosomes()

test_float = test_schedule.get_overall_fitness()

print test_float
