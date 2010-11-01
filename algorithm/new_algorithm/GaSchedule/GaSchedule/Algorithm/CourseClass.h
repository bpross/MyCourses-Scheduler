
////////////////////////////////////
// (C)2007-2008 Coolsoft Company. //
// All rights reserved.           //
// http://www.coolsoft-sd.com     //
// Licence: licence.txt           //
////////////////////////////////////

#include <list>
#include "Professor.h"
#include "StudentsGroup.h"
#include "Course.h"

#pragma once

using namespace std;

// Stores data about single class
class CourseClass
{

private:

	// Profesor who teaches
	Professor* _professor;

	// Course to which class belongs
	Course* _course;

	// Student groups who attend class
	list<StudentsGroup*> _groups;

	// Number of seats (students) required in room
	int _numberOfSeats;

	// Initicates wheather class requires computers
	bool _requiresLab;

	// Duration of class in hours
	int _duration;
	
public:

	// Initializes class object
	CourseClass(Professor* professor, Course* course, const list<StudentsGroup*>& groups,
		bool requiresLab, int duration);

	// Frees used memory
	~CourseClass();

	// Returns TRUE if another class has one or overlapping student groups.
	bool GroupsOverlap(const CourseClass& c ) const;

	// Returns TRUE if another class has same professor.
	inline bool ProfessorOverlaps(const CourseClass& c ) const { return *_professor == *c._professor; }

	// Return pointer to professor who teaches
	inline const Professor& GetProfessor() const { return *_professor; }

	// Return pointer to course to which class belongs
	inline const Course& GetCourse() const { return *_course; }

	// Returns reference to list of student groups who attend class
	inline const list<StudentsGroup*>& GetGroups() const { return _groups; }

	// Returns number of seats (students) required in room
	inline int GetNumberOfSeats() const { return _numberOfSeats; }

	// Returns TRUE if class requires computers in room.
	inline bool IsLabRequired() const { return _requiresLab; }

	// Returns duration of class in hours
	inline int GetDuration() const { return _duration; }

};
