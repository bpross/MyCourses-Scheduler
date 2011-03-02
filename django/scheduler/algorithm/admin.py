from django.contrib import admin
from scheduler.algorithm.models import *

admin.site.register(Business, BusinessAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Employer, EmployerAdmin)
admin.site.register(Employee)


