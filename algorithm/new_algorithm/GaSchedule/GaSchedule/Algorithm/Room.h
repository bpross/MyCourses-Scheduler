
////////////////////////////////////
// (C)2007-2008 Coolsoft Company. //
// All rights reserved.           //
// http://www.coolsoft-sd.com     //
// Licence: licence.txt           //
////////////////////////////////////

#include <string>

#pragma once

using namespace std;

// Stores data about classroom
class Room
{

private:

	// ID counter used to assign IDs automatically
	static int _nextRoomId;

private:

	// Room ID - automatically assigned
	int _id;

	// Room name
	string _name;

	// Inidicates if room has computers
	bool _lab;

	// Number of seats in room
	int _numberOfSeats;

public:

	// Initializes room data and assign ID to room
	Room(const string& name, bool lab, int numberOfSeats);

	// Returns room ID
	inline int GetId() const { return _id; }

	// Returns name
	inline const string& GetName() const { return _name; }

	// Returns TRUE if room has computers otherwise it returns FALSE
	inline bool IsLab() const { return _lab; }

	// Returns number of seats in room
	inline int GetNumberOfSeats() const { return _numberOfSeats; }

	// Restarts ID assigments
	static inline void RestartIDs() { _nextRoomId = 0; }

};
