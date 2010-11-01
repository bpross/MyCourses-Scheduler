
////////////////////////////////////
// (C)2007-2008 Coolsoft Company. //
// All rights reserved.           //
// http://www.coolsoft-sd.com     //
// Licence: licence.txt           //
////////////////////////////////////

#include "stdafx.h"
#include "Professor.h"

// Initializes professor data
Professor::Professor(int id, const string& name) : _id(id),
												   _name(name) { }

// Bind professor to course
void Professor::AddCourseClass(CourseClass* courseClass)
{
	_courseClasses.push_back( courseClass );
}

