#Course Scheduling Algorithm
#CMPS 115
#Linda Werner
#room.py


import sys

class Room:
        name = ''
	seat_num = 0
	lab = False
        #initializes room with ID and name
        def __init__(self, seat_num, lab, name = None):
		self.seat_num = seat_num
		self.lab = lab
                self.name = name

        #prints out the room data
        def print_room(self):
                print "(%d, %d, %s)" % (self.seat_num, self.lab, self.name)


if __name__ == '__main__':

        p1 = Room(50, True, "BE105")
        p1.print_room()
        sys.exit(0)

	
