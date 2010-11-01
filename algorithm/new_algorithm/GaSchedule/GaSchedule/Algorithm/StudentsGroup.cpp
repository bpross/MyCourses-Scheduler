
////////////////////////////////////
// (C)2007-2008 Coolsoft Company. //
// All rights reserved.           //
// http://www.coolsoft-sd.com     //
// Licence: licence.txt           //
////////////////////////////////////

#include "stdafx.h"
#include "StudentsGroup.h"

// Initializes student group data
StudentsGroup::StudentsGroup(int id, const string& name, int numberOfStudents) : _id(id),
																				 _name(name),
																				 _numberOfStudents(numberOfStudents)
{
}

// Bind group to class
void StudentsGroup::AddClass(CourseClass* courseClass)
{
	_courseClasses.push_back( courseClass );
}
