from django.contrib import admin
from scheduler.algorithm.models import *

admin.site.register(School, SchoolAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Prerequisite, PrerequisiteAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Period, PeriodAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(ClassInstance, ClassInstanceAdmin)
admin.site.register(ClassLab, ClassLabAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(PersonRole, PersonRoleAdmin)


