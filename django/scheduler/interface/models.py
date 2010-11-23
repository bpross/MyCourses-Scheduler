# CMPS 115 SCORE project
# Prof: Linda Werner
# 11-15-10


from django.db import models

# School:
# Holds: school ID number, school name
# Returns: The school name
class School(models.Model):
    idSchool = models.IntegerField(primary_key=True)
    SchoolName = models.CharField(max_length=45)

    def __unicode__(self):
        return self.SchoolName

# Department:
# Holds: the department ID, the department name, the deptartment's
#   abbreviated name, the department's  school ID
# Returns: The department name
class Department(models.Model):
    SchoolID = models.ForeignKey('School', to_field="idSchool")
    idDepartment = models.IntegerField(primary_key=True)
    DepartmentName = models.CharField(max_length=45)
    DeptAbbrv = models.CharField(max_length=11)

    def __unicode__(self):
        return self.DepartmentName

# Prerequisite:
# Holds: the prerequisite ID, the prerequisite's class ID
# Returns: nothing
class Prerequisite(models.Model):
    ClassID = models.ForeignKey('Class', to_field="idClass")
    idPrerequisite = models.IntegerField(primary_key=True)

# Class:
# Holds: the class ID, the class name, a description of the class, the class's department ID
# Returns: The class name
class Class(modles.Model):
    DepartmentID = models.ForeignKey('Department', to_field="idDepartment")
    idClass = models.IntegerField(primary_key=True)
    ClassName = models.CharField(max_length=45)
    ClassDescription = models.CharField(max_length=45)

    def __unicode__(self):
        return self.ClassName
    
# Buildings:
# Holds: the building ID, the building name
# Returns: The building name
class Buildings(models.Model):
    idBuilding = models.IntegerField(primary_key=True)
    BldgName = models.CharField(max_length=45)

    def __unicode__(self):
        return self.BldgName

# Room:
# Holds: the room ID, the room number, the type of room, the room name, the rooms' building ID
# Returns: The room name
class Room(models.Model):
    BuildingID = models.ForeignKey('Buildings', to_field="idBuilding")
    idRoom = models.IntegerField(primary_key=True)
    RoomNumber = models.CharField(max_length=45)
    Type = models.CharField(max_length=45)
    RoomName = models.CharField(max_length=45)
#	seat_num = models.IntegerField(primary_key=True)

    def __unicode__(self):
        return self.RoomName

# ClassLab:
# Holds: the lab ID, the lab name, the lab time, the lab's room ID, the lab's
#   building ID, the lab's class-instance ID
# Returns: The lab name

class ClassLab(models.Model):
    ClassInstanceID = models.ForiegnKey('ClassInstance', to_field"idClassInstance")
    idClassLab = models.IntegerField(primary_key=True)
    LabName = models.CharField(max_length=45)
    LabTime = models.CharField(max_length=45)
    RoomID = models.ForiegnKey('Room', to_field"idRoom")
    BuildingID = models.ForiegnKey('Building', to_field"idBuilding")

    def __unicode__(self):
        return self.LabName

# ClassInstance:
# Holds: the class-instance ID, the scheduled time, the section, the
#   class-instance's class ID, the class-instance's period ID
#   the class-instance's lecturer ID, the lecturer's office hours, the
#   TA's office hours, the TA's ID, the class-instance's building ID, the
#   class-instance's room ID
# Returns: Nothing
class ClassInstance(models.Model):
    ClassID = models.ForeignKey('Class', to_field"idClass")
    idClassInstance = models.IntegerField(primary_key=True)
    PeriodID = models.ForeignKey('Period', to_field"idPeriod")
    ClassTime = models.CharField(max_length=45)
    Section = models.CharField(max_length=45)
    LecturerID = models.ForeignKey('Lecturer', to_field"idLecturer")
    LecturerOfficeHours = models.CharField(max_length=45)
    TAOfficeHours = models.CharField(max_length=45)
    idTA = models.IntegerField(primary_key=True)
    BuildingID = models.ForeignKey('Building', to_field"idBuilding")
    RoomID = models.ForiegnKey('Room', to_field"idRoom")

# Lecturer:
# Holds: the lecturer ID, the lecturer's status, comments, the
#   lecturer's department ID
# Returns: Status
class Lecturer(models.Model):
    idLecturer = IntegerField(primary_key=True)
    Status = models.CharField(max_length=45)
    Comment = models.CharField(max_length=45)
    DepartmentID = models.ForeignKey('Department', to_field="idDepartment")

    def __unicode__(self):
        return self.Status
# Person:
# Holds: the person's ID, the persons's first name, middle initial, last
#   name, suffix and prefix
# Returns: The person's full title
class Person(models.Model):
    idPerson = models.IntegerField(primary_key=True)
    FName = models.CharField(max_length=45)
    MInitial = models.CharField(max_length=1)
    LName = models.CharField(max_length=45)
    Suffix = models.CharField(max_length=10)
    Prefix = models.CharField(max_length=10)

    def __unicode__(self):
        return u'%s %s %s %s %s' %  (self.Prefix, self.FName, self.MInitial, self.LName, self.Suffix)

# PersonRole:
# Holds: the Person-roles person ID and role ID
# Returns: Nothing
class PersonRole(models.Model):
    PersonID = models.ForiegnKey('Person', to_field"idPerson")
    RoleID = models.ForiegnKey('Role', to_field"idRole")

# Role:
# Holds: the role ID, the role name
# Returns: The role name
class Role(models.Model):
    idRole = models.IntegerField(primary_key=True)
    RoleName = models.CharField(max_length=45)

    def __unicode__(self):
        return self.RoleName






