from django.db import models

# Create your models here.

# Calendar
class inputShift(models.Model):
    idCal = models.IntegerField(null=True)
    title = models.CharField(max_length=45)
    start = models.DateTimeField(auto_now=False, auto_now_add=False)
    end   = models.DateTimeField(auto_now=False, auto_now_add=False)
    # positions necessary?
        def __unicode__(self):
        return self.idCal

class outputShift(models.Model):
	# Start
	# End
	# Title
	# People on this shift

class Week(models.Model):
	# one to many key to a bunch of shifts.

class Month(models.Model):
	# A month should own several weeks?
	# But what about weeks that fall across months?
