#tests room.py
#Author: Erik Steggall
#Author: Will Crawford
"""
This is a unit test of room.py
It tests various methods of the Room class.
"""
from room import Room

# Test direct room population
# Input: 100 seats, no lab, name BE
# Expected output: (100, 0, BE) 
r1 = Room(100, False, 'BE')
r1.print_room()

# Input: 0 seats, no lab, name BE
# Expected output: (0, 0, BE) 
r1 = Room(0, False, 'BE')
r1.print_room()

# Input: 100000000000 seats, no lab, name BE
# Expected output: (100000000000, 0, BE)
r1 = Room(100000000000, False, 'BE')
r1.print_room()

# Input: 100 seats, lab, name BE
# Expected output: (100, 1, BE)
r1 = Room(100, True, 'BE')
r1.print_room()

# Input: 150 seats, lab, no name
# Expected output: (150, 1, None)
r1 = Room(150, True)
r1.print_room()


# Test setting the ID
# Input: 1
# Expected output: 1
r1.id = 1
print r1.get_id()

# Test default constructor's data population
# Input: just call Room()
# Expected output: TypeError (Insufficient data to print)
r2 = Room()
try:
	r2.print_room()
except TypeError:
	print "Exception caught: TypeError; test successful"

# Test manipulation functions
# Input: 200 seats, lab, name Baskin
# Expected output: (200, 1, Baskin)
r2.add_seats(200)
r2.add_name('Baskin')
r2.add_lab(True)
r2.print_room()

# Test access functions
# Input: Call access functions
# Expected output:
# 200
# True
# Baskin
print r2.get_seat_num()
print r2.lab_status()
print r2.get_name()
