from django.db import models
import scheduler.algorithm.models as algomodels

# Create your models here.

# Employee
class Person(models.Model):
    business = models.ForeignKey(algomodels.Business)
    name = models.CharField(primary_key=True, max_length=45)
    # This should be a foreign key to an employee field, shouldn't it?
    # Otherwise we're duplicating data.
    position = models.CharField(max_length=45)
    # This should be a foreign key to an employee field, shouldn't it?
    # Otherwise we're duplicating data.
    def __unicode__(self):
        return self.name

# Shift to go into scheduler
class inputShift(models.Model):
    title = models.CharField(primary_key=True, max_length=45)
    business = models.ForeignKey(algomodels.Business)
    start = models.DateTimeField(auto_now_add=False)
    end   = models.DateTimeField(auto_now=False, auto_now_add=False)
    #people = models.ManyToManyField(Person) 
    # We don't need this until we enable manual assignment
    # on scheduler input.
    position = models.CharField(max_length=45)
    def __unicode__(self):
        return self.title

# Shift outputted by scheduler
class outputShift(models.Model):
    title = models.CharField(primary_key=True, max_length=45)
    business = models.ForeignKey(algomodels.Business)
    start = models.DateTimeField(auto_now=False, auto_now_add=False)
    end   = models.DateTimeField(auto_now=False, auto_now_add=False)
    people = models.ManyToManyField(Person) 
    position = models.CharField(max_length=45)
    def __unicode__(self):
        return self.title

# Day
class inputDay(models.Model):
    name = models.CharField(primary_key=True, max_length=45)
    business = models.ForeignKey(algomodels.Business)
    shifts = models.ManyToManyField(inputShift)
    def __unicode__(self):
        return self.name
        
class outputDay(models.Model):
    name = models.CharField(primary_key=True, max_length=45)
    business = models.ForeignKey(algomodels.Business)
    shifts = models.ManyToManyField(outputShift)
    def __unicode__(self):
        return self.name


# Week
class inputWeek(models.Model):
    business = models.ForeignKey(algomodels.Business)
    start = models.DateTimeField(auto_now_add=False)
    end   = models.DateTimeField(auto_now=False, auto_now_add=False)
    days  = models.ManyToManyField(inputDay)

class outputWeek(models.Model):
    business = models.ForeignKey(algomodels.Business)
    start = models.DateTimeField(auto_now_add=False)
    end   = models.DateTimeField(auto_now=False, auto_now_add=False)
    days  = models.ManyToManyField(outputDay)
    
    
