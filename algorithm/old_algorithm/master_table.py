#!/usr/bin/local/python
#Author: Benjamin Ross(bpross)
#Date: 10/25

"""
This file creates the master table from all of the class/room data

It works like so:
It reads in the class_files one at a time and puts them into the master
table. The master table is a list of lists with priority queues as the data.
These priority queues store lists formatted as so:
[class_name,fitness]. The top class will have the highest fitness

The file will be printed as so:

Time|Class1|....|ClassN
1   | Topfit|.....|Topfit
2   |Topfit|...........
......................

And a file will be created for all of the possible schedules the whole way down
the queue. So there will be the same number of schedules as there are rooms

Room File Format:
Room_Number
"""

from queue import Queue
from room_table import RoomTable
import os


class MasterTable:
    
    master_table = []
    room_tables = []
    room_list = []

    """
    Initializes the Class
    @param room_master: file that contains all of the rooms
    """
    def __init__(self,room_master):
        self.room_file = room_master

    """
    Creates an empty master table
    @param hours: largest possible hour (ie 13)
    """
    def create_empty(self, hours):
    
        count = 1
        while count <= hours:
            row = [count]
            for iter in range(len(self.room_list)):
                empty = Queue()
                row.append(empty)
            self.master_table.append(row)
            count += 1

    """
    Reads in the room file and adds the values to room_list
    """
    def get_rooms(self):

        file = open(self.room_file , 'r')
        file_list = file.readlines()

        for rooms in range (len(file_list)):
            line = file_list[rooms].split()

            self.room_list.insert(rooms,line[0])

    """
    Reads in all of the room_tables and adds them to the room_tables list
    """
    def get_room_tables(self):
        cur_dir = os.getcwd()
        cur_dir = cur_dir + "/room_tables"

        count = 0
        file_list = []
        for filename in os.listdir(cur_dir):
            if 'table' in filename:
                filename = cur_dir + '/' + filename
                file_list.insert(count, filename)
                count += 1

        for iter in range(len(file_list)):
            self.room_tables.append(RoomTable())
        
        for count in range(len(file_list)):
            self.room_tables[count].read_from_file(file_list[count])
            print self.room_tables[count]
            print count

    """
    Creates the master table from the room_tables
    """
    def create_master(self):
        
        for table in self.room_tables:
            data = table.room_table
            first_row = data[0]
            count = 1
            while count in range(len(data)):
                line = data[count]

                iter = 1
                while iter in range(len(line)):
                    print first_row
                    fitness = line[iter]

                    master_index = first_row[iter]
                    queue = self.master_table[count[master_index]]

                    queue.insert([data.class_name,fitness])

                    iter += 1

                count += 1

    def print_master(self):
        for num in range(len(self.master_table)):
            row = self.master_table[num]
            for iter in range(len(row)):
                if num is 0:
                    print row[iter]

                else:
                    if iter is 0:
                        print row[iter]

                    else:
                        queue = row[iter]
                        queue.print_queue


test = MasterTable('room_file')
test.get_rooms()
test.get_room_tables()
test.create_master()
test.print_master()
