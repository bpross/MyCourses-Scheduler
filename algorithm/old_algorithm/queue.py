#!/usr/local/bin/python
#Author: Benjamin Ross(bpross)
#Date: 10/25

"""
This file implements a priority queue in python
The linked list data structure is used as the underlying data structure
"""
from list import List

class Queue:

    def __init__(self):
        self.list = List()


    """
    Inserts data into the correct position in the queue
    Based on the assumption that the data given is in the format:
    [class_name,fitness]
    The higher the fitness, the closer the class will be to the front
    """
    def insert(self,data):
        queue = self.list

        #If queue is empty, insert at the first element
        if queue.is_empty():
            queue.insert_before_first(data)

        #Queue is not empty, iterate through to find spot for new element
        else:
            queue.move_first()
            temp = queue.get_current()
            while temp[1] <= data[1] and queue.current.next is not None:
                queue.move_next()
                temp = queue.get_current()
                
            queue.insert_after_current(data)

    """
    Prints the Queue
    """
    def print_queue(self):
        self.list.print_list()
