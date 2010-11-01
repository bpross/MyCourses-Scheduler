#!/usr/local/bin/python
#Author: Benjamin Ross(bpross)
#Date: 10/25

"""
This File implements a linked list in python
Code taken from List.java I implemented for CS 101 with Prof. Tantalo
"""

class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

class List:

    def __init__(self):
        self.front = None
        self.back = None
        self.current = None
        self.length = 0

    ###Access Functions###

    #Returns true if the List has no elements
    def is_empty(self):
        if self.length is 0:
            return True
        else:
            return False

    #Returns true of current is None
    def off_end(self):
        if self.current is None:
            return True
        else:
            return False

    #Returns true if the first element is current
    #Pre: !is_empty()
    def at_first(self):
        if self.is_empty():
            sys.stderr.write('Cannot Access Empty List')
        
        else:
            if self.current is self.front:
                return True
            else:
                return False

    #Returns true if last element is current
    #Pre: !is_empty()
    def at_last(self):
        if self.is_empty():
            sys.stderr.write('Cannot Access Empty List')

        else:
            if self.current is self.back:
                return True
            else:
                return False

    #Returns the first element
    #Pre: !is_empty
    def get_first(self):
        if self.is_empty():
            sys.stderr.write('Cannot Access Empty List')

        else:
            return self.front.data

    #Returns the last element
    #Pre: !is_empty()
    def get_last(self):
        if self.is_empty():
            sys.stderr.write('Cannot Access Empty List')

        else:
            return self.back.data

    #Returns current element
    #Pre: !is_empty()
    def get_current(self):
        if self.is_empty():
            sys.stderr.write('Cannot Access Empty List')

        else:
            return self.current.data


    #Returns the length of the list
    def get_length(self):
        return self.length



    ###Manipulation Functions###

    #Sets this List to the empty state
    #Post: is_emtpy()
    def make_empty(self):
        self.front = None
        self.back = None
        self.current = None
        self.length = 0

    #Sets current marker to first element
    #Pre: ! is_empty()
    #Post: !off_end()
    def move_first(self):
        if self.is_empty():
            sys.stderr.write('Cannot Access Empty List')

        else:
            self.current = self.front

    #Moves current marker to last element
    #Pre: !is_empty()
    #Post: !off_end()
    def move_last(self):
        if self.is_empty():
            sys.stderr.write('Cannot Access Empty List')

        else:
            self.current = self.back

    #Moves current marker one step toward first element
    #Pre: !is_empty()
    #Post: !off_end()
    def move_prev(self):
        if self.is_empty():
            sys.stderr.write('Cannot Access Empty List')

        else:
            self.current = self.current.previous

    #Moves current marker one step toward last element
    #Pre: !is_empty()
    #Post: !off_end()

    def move_next(self):
        if self.is_empty():
            sys.stderr.write('Cannot Access Empty List')

        else:
            self.current = self.current.next


    #Inserts new element before first element
    #Post: !is_empty()
    def insert_before_first(self,data):
        temp = Node()

        if self.front is None:
            self.front = Node(data)
            self.back = self.front
            self.length += 1

        else:
            new_node = Node(data)
            new_node.next = self.front
            self.front.previous = new_node
            self.front = new_node
            self.length +=1

        if self.length > 1:
            temp = self.back
            while temp.next is not None:
                temp = temp.next
            self.back = temp

    #Inserts new element after last element
    #Post: !off_end()
    def insert_after_last(self,data):
        temp = self.back

        if self.back is None:
            self.back = Node(data)
            self.length += 1

        else:
            self.back = self.back.next
            self.back = Node(data)
            temp.next = self.back
            self.back.previous = temp
            self.length += 1

        if self.length > 1:
            temp = self.back
            while(temp.previous is not None):
                temp = temp.previous
                self.front = temp


    #Inserts new element before current element
    #Pre: !is_empty() & !off_end()
    def insert_before_current(self,data):
        if self.is_empty():
            sys.stderr.write('Cannot Access Empty List')

        elif self.off_end():
            sys.stderr.write('insert_before_current: Cannot Access Empty List')

        else:
            new_node = Node(data)
            self.current.previous.next = new_node
            new_node.next = self.current
            self.current.previous = new_node
            self.length += 1

    #Inserts new element after current element
    #Pre: !is_empty() & !off_end()
    def insert_after_current(self,data):
        if self.is_empty():
            sys.stderr.write('Cannot Access Empty List')

        elif self.off_end():
            sys.stderr.write('insert_after_current: Cannot Access Empty List')

        else:
            new_node = Node(data)
            if(self.current.next != None):
                self.current.next.previous = new_node
            new_node.next = self.current.next
            self.current.next = new_node
            self.length += 1

        if self.length > 1:
            temp = self.front
            while(temp.next is not None):
                temp = temp.next
            self.back = temp

        #Deletes first element
        #Pre: !is_empty()
    def delete_first(self):
        if self.is_empty():
            sys.stderr.write('Cannot Access Empty List')
            
        else:
            self.front = self.front.next
            if self.front is not None:
                self.front.previous = None
                self.length -= 1

        #Deletes last element
        #Pre: !is_empty()
    def delete_last(self):
        if self.is_empty():
            sys.stderr.write('Cannont Access Empty List')
            
        else:
            self.back = self.back.previous
            self.back.next = None
            self.length -= 1

        #Deletes current element
        #Pre: !is_empty() & !off_end()
        #Post: off_end()
    def delete_current(self):
        if self.is_empty():
            sys.stderr.write('Cannot Access Empty List')

        elif self.off_end():
            sys.stderr.write('delete_current: Cannot Access Empty List')

        else:
            self.current.previous.next = self.current.next
            self.current.next.previous = self.current.previous
            self.current = None
            self.length -= 1


    def print_list(self):
            temp = self.front
            while temp is not None:
                print temp.data
                temp = temp.next
            

        
