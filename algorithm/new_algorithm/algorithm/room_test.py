#tests room.py



from room import Room

seats = 0
lab = 0
name = 's'

r1 = Room(100, False, 'BE')
r2 = Room()

r2.add_seats(200)
r2.add_name('Baskin')
r2.add_lab(True)

seats = r2.get_seat_num()
lab = r2.lab_status()
name = r2.get_name()

r1.print_room()
r1.id = 1

test = r1.get_id()
print test 

print "Seats: %d,\nLab: %d,\nName: %s\n" % (seats, lab, name)
