#!/usr/local/bin/python
#Author: Benjamin Ross(bpross)
#Date: 10/22

"""
This file creates a room table for each class.
The table is layed out as follows:

Time|Room1|.....|RoomN|
----------------------
8AM |     |     |     |
.
.
.
.
.
12AM|     |     |     |

The first row and column are not used to store fitness
values.

*************************
How Fitness is Calculated
*************************
First the room size is taken into consideration:
Difference    Score
0-5           10
6-10          9
11-15         8
16-20         7
21-25         6
26-30         5
31-35         4
36-40         3
41-45         2
46+           1

1 is the lowest score, because you can still have class
in that room(super inefficiently)

Next is Time. Time is a given bonus. Time is the range
1-n, where 1 corresponds to the first class time and
n corresponds to the last class time
i.e. 8AM = 1, 8PM=13 where classes are every hour
Class time will be a range from earliest time slot
to latest time slot. If the Time is in the class
time range, then a +10 bonus is given, else +0

Room File Format:
Room_Number   Size

Class File Format:
Class_name
Class_size
Start Range   Finish Range

"""

class RoomTable:

    """
    Variables
    @room_sizes: dictionary that, where room_name: room_size
    @times: all valid times for class
    @class_name: name of the class
    @class_time: class Time Range
    @room_table: table that is created with fitness'
    """
    room_sizes = {}
    num_rooms = 0
    room_list = []
    times = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    class_name = ''
    class_size = 0
    class_time = []
    room_table = []

    """
    Initializes the Class
    @param class_file: file where class info is stored
    @param room_file: file where room info is stored
    """
    def __init__(self, class_file, room_file):
        self.class_file = class_file
        self.room_file = room_file

    """
    Reads the room_file and adds values to room_sizes
    """
    def get_room_info(self):

        file = open(self.room_file, 'r')
        file_list = file.readlines()
        
        for rooms in range (len(file_list)):
            line = file_list[rooms].split()
            if self.room_sizes.has_key(line[0]):
                self.room_sizes.append(line[1])
            else:
                self.room_sizes[line[0]] = [line[1]]
                self.room_list.insert(rooms,line[0]) 
                self.num_rooms = self.num_rooms + 1

    """
    Reads the class_file and assigns class_name, class_size
    and class_time
    """
    def get_class_info(self):

        file = open(self.class_file, 'r')
        file_list = file.readlines()
        
        self.class_name = file_list[0].rstrip()
        self.class_size = int(file_list[1].rstrip())
        range = file_list[2].split()
        count = int(range[0])
        while count <= int(range[1]):
            self.class_time.append(count)
            count = count + 1

    """
    Calculates the fitness of the roomXtime
    @param room_number: room number, used to get room size
    @param time: the current time row
    """
    def calculate_fitness(self, room_number, time):
        fitness = 0
        room_size = self.room_sizes[room_number]
        size = room_size[0]
        size_diff = int(size) - self.class_size
        if size_diff <= 5:
            fitness = fitness + 10
        elif size_diff <= 10:
            fitness = fitness + 9
        elif size_diff <= 15:
            fitness = fitness + 8
        elif size_diff <= 20:
            fitness = fitness + 7
        elif size_diff <= 25:
            fitness = fitness + 6
        elif size_diff <= 30:
            fitness = fitness + 5
        elif size_diff <=35:
            fitness = fitness + 4
        elif size_diff <= 40:
            fitness = fitness + 3
        elif size_diff <= 45:
            fitness = fitness + 2
        elif size_diff > 45:
            fitness = fitness + 1

        if time in self.class_time:
            fitness = fitness + 10

        return fitness
    
    """
    Adds a new row to the room_table
    @param new_row: row being added to room_table
    """
    def add_to_table(self, new_row):
        self.room_table.append(new_row)

    def print_to_file(self,outfile):
        out = open(outfile, 'w')
        for index in range(len(self.room_table)):
            row = self.room_table[index]
            for element in range(len(row)):
                word = str(row[element]) + " "
                out.write(word)
                element = element + 1
            out.write("\n")
            index = index + 1

import sys
import optparse

def main():  
    # Get files from Command Line
    parser = optparse.OptionParser("usage: %prog [options] classfile roomfile\
                                                           outfile")
    parser.add_option("-c", "--class", dest="class_file",
                      type="string")
    parser.add_option("-r", "--room", dest="room_file",
                      type="string")
    parser.add_option("-o", "--out", dest="outfile",
                      type="string")
    
    (options, args) = parser.parse_args()

    class_file = options.class_file
    room_file = options.room_file
    outfile = options.outfile
            
    table = RoomTable(class_file, room_file)
    table.get_room_info()
    table.get_class_info()
    row = ["Time"]
    row = row + table.room_list
    table.add_to_table(row)

    for time in range(len(table.times)):
        class_time = table.times[time]
        new_row = [class_time]
        count = 0
        while count < table.num_rooms:
            fitness = table.calculate_fitness(table.room_list[count],
                                              class_time)
            new_row.append(fitness)
            count = count + 1
        table.add_to_table(new_row)
        
    print table.room_table
    table.print_to_file(outfile)

main()
