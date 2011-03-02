import csv
from scheduler.algorithm.models import Business, Building, Employer, Employee

class CSV:

    def csv_import(self, file = None, flag = None):
        if file is None:
            print "Error: Need file to parse"
            return False
        if flag is None:
            print "Error: File type needs to be specified!"
            return False
        else:
            if flag is "business":
                return self.store_business(file)
            elif flag == "building":
                return self.store_building(file)
            elif flag == "employer":
                return self.store_employer(file)
            elif flag == "employee":
                return self.store_employee(file)
            else:
                print "invalid type: type given is %s"%(flag)
                return False

    def store_business(self, filename = None):
        businessReader = csv.reader(filename,delimiter = ',', quotechar = '|')
        for row in businessReader:
            new_business = Business(idBusiness = row[0], business_name = row[1]) 
            # Letting users import id is probably a problem.
            new_business.save()
        return True

	def store_building(self, filename = None):
		buildingReader = csv.reader(filename, delimiter = ',', quotechar = '|')
		for row in buildingReader:
			new_building = Building(idBuilding = row[0], building_name = row[1])
			new_building.save()
		return True

	def store_employer(self, filename = None):
		employerReader = csv.reader(filename, delimiter = ',', quotechar = '|')
		for row in employerReader:
			new_employer = Employer(idEmployer = row[0], employer_name = row[1], idBusiness = row[2])
			# Instead of pulling idBusiness from the file, we should pull it from the current user account.
			new_employer.save()
		return True

	def store_employee(self, filename = None):
		employeeReader = csv.reader(filename, delimiter = ',', quotechar = '|')
		for row in employeeReader:
			new_employee = Employee(idEmployee = row[0], employee_first_name = row[1], 
				employee_middle_name = row[2], employee_last_name = row[3], 
				employee_position = row[4], idBusiness = row[5])
			# Instead of pulling idBusiness from the file, we should pull it from the current user account.
			new_employee.save()
		return True

'''
    def print_database(self):
        from scheduler.algorithm import models
        from scheduler.algorithm.models import School, Department, Class, Prerequisite, Building,  Room, Period, Lecturer, ClassInstance, ClassLab, Person, Role, PersonRole
        print "                         Contents of Database "
        all_schools = School.objects.all()
        if(all_schools !=None):
            for School in all_schools:
                print "School: %s, School ID: %d " % (School.School, School.idSchool)

        all_departments = Department.objects.all()
        if(all_departments != None):
            for Department in all_departments:
                print "Department: %s, Department ID: %d " % (Department.Department, Department.idDepartment)

        all_buildings = Building.objects.all()
        if(all_buildings != None):
            for Building in all_buildings:
                print "Building: %s, Building ID: %d " % (Building.BldgName, Building.idBuilding)
        all_class_instance = ClassInstance.objects.all()
        if (all_class_instance != None):
            for ClassInstance in all_class_instance:
                lecturer = ClassInstance.idLecturer
                course = ClassInstance.idClass
                print "Course Schedule(professor: %s Course: %s)" % (lecturer.Name, course.Class)

        all_lecturers = Lecturer.objects.all()
        if (all_lecturers != None):
            for Lecturer in all_lecturers:
                print "Lecturer name: %s, Lecturer ID: %d" % (Lecturer.Name, Lecturer.idLecturer)

        all_rooms = Room.objects.all()
        if (all_rooms != None):
            for Room in all_rooms:
                print "Room: %s, Room ID: %d seats: %d" % (Room.RoomName, Room.idRoom, Room.SeatNum)

        all_courses = Class.objects.all()
        if (all_courses != None):
            for Class in all_courses:
                print "Course: %s, Course ID: %d " % (Class.Class, Class.idClass)
'''