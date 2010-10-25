#!/usr/local/bin/python
#Author: Benjamin Ross(bpross)
#Date: 10/25

"""
Test for the queue ADT
"""
from queue import Queue

test = Queue()
list = [['z',4],['a',1],['b',2],['c',3]]
for classes in list:
    test.insert(classes)
test.print_queue()
