from django.contrib import admin
from scheduler.thecal.models import *

admin.site.register(Person, PersonAdmin)
admin.site.register(inputShift, inputShiftAdmin)
admin.site.register(outputShift, outputShiftAdmin)
admin.site.register(inputDay)
admin.site.register(outputDay)
admin.site.register(inputWeek, inputWeekAdmin)
admin.site.register(outputWeek, outputWeekAdmin)
