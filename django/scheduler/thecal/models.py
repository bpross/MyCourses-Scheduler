from django.db import models

# Create your models here.

# Calendar
class Calendar(models.Model):
    idCal = models.IntegerField(null=True)
    title = models.CharField(max_length=45)
    start = models.DateTimeField(auto_now=False, auto_now_add=False)
    end   = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __unicode__(self):
        return self.idCal
