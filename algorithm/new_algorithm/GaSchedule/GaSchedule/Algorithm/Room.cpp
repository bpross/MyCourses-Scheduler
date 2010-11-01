
////////////////////////////////////
// (C)2007-2008 Coolsoft Company. //
// All rights reserved.           //
// http://www.coolsoft-sd.com     //
// Licence: licence.txt           //
////////////////////////////////////

#include "stdafx.h"
#include "Room.h"

int Room::_nextRoomId = 0;

// Initializes room data and assign ID to room
Room::Room(const string& name, bool lab, int numberOfSeats) : _id(_nextRoomId++),
																	  _name(name),
																	  _lab(lab),
																	  _numberOfSeats(numberOfSeats) { }
