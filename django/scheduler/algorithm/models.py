# CMPS 115 SCORE project
# Prof: Linda Werner
# 11-15-10

from django.db import models
from django.contrib import admin

# School:
# Holds: school ID number, school name
# Returns: The school name
class School(models.Model):
    idSchool = models.IntegerField(primary_key=True)
    School = models.CharField(max_length=45)

    def __unicode__(self):
        return self.School

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('idSchool', 'School')
    list_filter = ('idSchool', 'School')

# Department:
# Holds: the department ID, the department name, the deptartment's
#   abbreviated name, the department's  school ID
# Returns: The department name
class Department(models.Model):
    idSchool = models.ForeignKey(School, to_field='idSchool')
    idDepartment = models.IntegerField(primary_key=True)
    Department = models.CharField(max_length=45)
    DeptAbbrev = models.CharField(max_length=11)

    def __unicode__(self):
        return self.Department

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('idSchool', 'idDepartment', 'Department', 'DeptAbbrev')
    list_filter = ('idSchool', 'idDepartment', 'Department', 'DeptAbbrev')

# Class:
# Holds: the class ID, the class name, a description of the class, the class's department ID
# Returns: The class name
class Class(models.Model):
    idDepartment = models.ForeignKey(Department, to_field='idDepartment')
    idClass = models.IntegerField(primary_key=True)
    Class = models.CharField(max_length=45)
    ClassDescription = models.TextField()

    def __unicode__(self):
        return self.Class

class ClassAdmin(admin.ModelAdmin):
    list_display = ('idDepartment', 'idClass', 'Class', 'ClassDescription')
    list_filter = ('idDepartment', 'idClass', 'Class', 'ClassDescription')

# Prerequisite:
# Holds: the prerequisite ID, the prerequisite's class ID
# Returns: nothing
class Prerequisite(models.Model):
    idPrereq = models.IntegerField(primary_key=True)
    ClassID = models.ForeignKey(Class, to_field='idClass')

class PrerequisiteAdmin(admin.ModelAdmin):
    list_display = ('idPrereq', 'ClassID')
    list_filter = ('idPrereq', 'ClassID')

# Building:
# Holds: the building ID, the building name
# Returns: The building name
class Building(models.Model):
    idBuilding = models.IntegerField(primary_key=True)
    BldgName = models.CharField(max_length=45)

    def __unicode__(self):
        return self.BldgName

class BuildingAdmin(admin.ModelAdmin):
    list_display = ('idBuilding', 'BldgName')
    list_filter = ('idBuilding', 'BldgName')

# Room:
# Holds: the room ID, the room number, the type of room, the room name, the rooms' building ID
# Returns: The room name
class Room(models.Model):
    idBuilding = models.ForeignKey(Building, to_field='idBuilding')
    idRoom = models.IntegerField(primary_key=True)
    RoomNumber = models.CharField(max_length=45)
    Type = models.CharField(max_length=45)
    RoomName = models.CharField(max_length=45)
    Lab = models.BooleanField(default=False)
    SeatNum = models.IntegerField(default=45)
#	seat_num = models.IntegerField(primary_key=True)

    def __unicode__(self):
        return self.RoomName

class RoomAdmin(admin.ModelAdmin):
    list_display = ('idBuilding', 'idRoom', 'RoomNumber', 'Type', 'RoomName', 'Lab', 'SeatNum')
    list_filter = ('idBuilding', 'idRoom', 'RoomNumber', 'Type', 'RoomName', 'Lab', 'SeatNum')
#   append seat_num to display/filter lists if uncommented in class above

# Period:
# Holds: 
# Returns:

class Period(models.Model):
    idPeriod = models.IntegerField(primary_key=True)
    period = models.CharField(max_length=45)
    StartDate = models.DateField()
    EndDate = models.DateField()
    InstructionBegins = models.DateField()
    InstructionEnds = models.DateField()

class PeriodAdmin(admin.ModelAdmin):
    list_display = ('idPeriod', 'period', 'StartDate', 'EndDate', 'InstructionBegins', 'InstructionEnds')
    list_filter = ('idPeriod', 'period', 'StartDate', 'EndDate', 'InstructionBegins', 'InstructionEnds')

# Lecturer:
# Holds: the lecturer ID, the lecturer's status, comments, the
#   lecturer's department ID
# Returns: Status
class Lecturer(models.Model):
    idLecturer = models.IntegerField(primary_key=True)
    Status = models.CharField(max_length=45)
    Name = models.CharField(max_length=45)
    Comment = models.TextField()
    idDepartment = models.ForeignKey(Department, to_field='idDepartment')

    def __unicode__(self):
        return self.Name

class LecturerAdmin(admin.ModelAdmin):
    list_display = ('idLecturer', 'Status', 'Name', 'Comment', 'idDepartment')
    list_filter = ('idLecturer', 'Status', 'Name', 'Comment', 'idDepartment')

# ClassInstance:
# Holds: the class-instance ID, the scheduled time, the section, the
#   class-instance's class ID, the class-instance's period ID
#   the class-instance's lecturer ID, the lecturer's office hours, the
#   TA's office hours, the TA's ID, the class-instance's building ID, the
#   class-instance's room ID
# Returns: Nothing
class ClassInstance(models.Model):
    idClass = models.ForeignKey(Class, to_field='idClass')
    idClassInstance = models.IntegerField(primary_key=True)
    idPeriod = models.ForeignKey(Period, to_field='idPeriod')
    ClassTime = models.CharField(max_length=45)
    Section = models.CharField(max_length=45)
    idLecturer = models.ForeignKey(Lecturer, to_field='idLecturer')
    LecturerOfficeHours = models.CharField(max_length=45, null=True)
    TAOfficeHours = models.CharField(max_length=45, null=True)
    idTA = models.IntegerField(null=True)
    idBuilding = models.ForeignKey(Building, to_field='idBuilding')
    idRoom = models.ForeignKey(Room, to_field='idRoom')

class ClassInstanceAdmin(admin.ModelAdmin):
    list_display = ('idClass', 'idClassInstance', 'idPeriod', 'ClassTime', 'Section', 'idLecturer', 'LecturerOfficeHours', 'TAOfficeHours', 'idTA', 'idBuilding', 'idRoom')
    list_filter = ('idClass', 'idClassInstance', 'idPeriod', 'ClassTime', 'Section', 'idLecturer', 'LecturerOfficeHours', 'TAOfficeHours', 'idTA', 'idBuilding', 'idRoom')

# ClassLab:
# Holds: the lab ID, the lab name, the lab time, the lab's room ID, the lab's
#   building ID, the lab's class-instance ID
# Returns: The lab name
class ClassLab(models.Model):
    idClassInstance = models.ForeignKey(ClassInstance, to_field='idClassInstance')
    idClassLab = models.IntegerField(primary_key=True)
    LabName = models.CharField(max_length=45)
    LabTime = models.CharField(max_length=45)
    idRoom = models.ForeignKey(Room, to_field='idRoom')
    idBuilding = models.ForeignKey(Building, to_field='idBuilding')

    def __unicode__(self):
        return self.LabName

class ClassLabAdmin(admin.ModelAdmin):
    list_display = ('idClassInstance', 'idClassLab', 'LabName', 'idRoom', 'idBuilding')
    list_filter = ('idClassInstance', 'idClassLab', 'LabName', 'idRoom', 'idBuilding')

# Person:
# Holds: the person's ID, the persons's first name, middle initial, last
#   name, suffix and prefix
# Returns: The person's full title
class Person(models.Model):
    idPerson = models.IntegerField(primary_key=True)
    FName = models.CharField(max_length=45)
    MInitial = models.CharField(max_length=1, null=True)
    LName = models.CharField(max_length=45)
    Suffix = models.CharField(max_length=10, null=True)
    Prefix = models.CharField(max_length=10, null=True)

    def __unicode__(self):
        return self.LName

class PersonAdmin(admin.ModelAdmin):
    list_display = ('idPerson', 'FName', 'MInitial', 'LName', 'Suffix', 'Prefix')
    list_filter = ('idPerson', 'FName', 'MInitial', 'LName', 'Suffix', 'Prefix')

# Role:
# Holds: the role ID, the role name
# Returns: The role name
class Role(models.Model):
    idRole = models.IntegerField(primary_key=True)
    Role = models.CharField(max_length=45)

    def __unicode__(self):
        return self.Role

class RoleAdmin(admin.ModelAdmin):
    list_display = ('idRole', 'Role')
    list_filter = ('idRole', 'Role')

# PersonRole:
# Holds: the Person-roles person ID and role ID
# Returns: Nothing
class PersonRole(models.Model):
    idPerson = models.ForeignKey(Person, to_field='idPerson')
    idRole = models.ForeignKey(Role, to_field='idRole')

class PersonRoleAdmin(admin.ModelAdmin):
    list_display = ('idPerson', 'idRole')
    list_filter = ('idPerson', 'idRole')
