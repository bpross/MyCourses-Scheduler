#!/usr/local/bin/python
#Author: Benjamin Ross(bpross)
#Date: 10/23

"""
This file tests the List class in list.py
"""
from list import List

new_list = List()
bool = new_list.is_empty()
print bool
bool = new_list.off_end()
print bool
test_data = [1,2,3,4,5,6,7,8]
for num in test_data:
    new_list.insert_before_first(num)
print new_list.is_empty()
for num in test_data:
    new_list.insert_after_last(num)
print new_list.length
new_list.print_list()
new_list.make_empty()
bool = new_list.is_empty()
print bool
for num in test_data:
    new_list.insert_after_last(num)
new_list.print_list()
new_list.move_first()
bool = new_list.at_first()
print bool
temp = new_list.get_first()
print temp
temp = new_list.get_last()
print temp
bool = new_list.off_end()
print bool

new_list.move_last()
new_list.move_prev()
temp = new_list.get_current()
print temp
new_list.insert_after_current(1)
new_list.print_list()
new_list.insert_before_current(2)
new_list.print_list()
