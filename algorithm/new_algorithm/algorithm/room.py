#Course Scheduling Algorithm
#CMPS 115
#Linda Werner
#room.py
#Author: egall24, bpross

import sys

class Room:
	
        #initializes room with ID and name
        def __init__(self, seat_num = None, lab = None, name = None):
		if seat_num is None:
			self.seat_num = None
		else:
			self.seat_num = seat_num
		if lab is None:
			self.lab = None
		else:
			self.lab = lab
		if name is None:
			self.name = None
		else:
			self.name = name


	#Returns the seat number of the room
	def get_seat_num(self):
		return self.seat_num

	#Adds/changes the seat number of the room
	def add_seats(self, seat_num):
		self.seat_num = seat_num
		
	#Returns the Name of the Room
	def get_name(self):
		return self.name

	#Adds/changes the name of the room
	def add_name(self,name):
		self.name = name
		
	#Returns True if Room has lab, False if no Lab
	def lab_status(self):
		return self.lab

	#Adds/changes the lab status of the room
	def add_lab(self,lab):
		self.lab = lab
		
        #prints out the room data
        def print_room(self):
                print "(%d, %d, %s)" % (self.seat_num, self.lab, self.name)


if __name__ == '__main__':

        p1 = Room(50, True, "BE105")
        p1.print_room()
        sys.exit(0)

	
