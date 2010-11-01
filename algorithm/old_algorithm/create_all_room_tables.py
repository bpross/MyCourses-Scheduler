#!/usr/local/bin/python
#Author: Benjamin Ross(bpross)
#Date: 10/23

"""
This file loops over every class file and creates and saves a room table

The location of the class files is /classes with respect to the current
location (meaning it isnt under root)

Currently it is using only one room file, but once integrated with django
this file will make a dynamic room file for the classes. Never saving the
room file will make it use less space.
"""

import os

#Get the current directory 
cur_dir = os.getcwd()

cur_dir = cur_dir + "/classes"

#Create a list of all of the class files
count = 0
file_list = []

for filename in os.listdir(cur_dir):
    file_list.insert(count, filename)


#Create a room table for all of the files
for file in file_list:
    if str(file) != ".svn":
        print str(file)
        outfile ="room_tables/" + str(file) + "_table"
        file = "classes/" + file
        run_str = "python room_table.py -c " + file +" -r room_file -o " + outfile
        os.system(run_str)
