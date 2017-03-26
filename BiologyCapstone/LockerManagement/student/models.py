from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

# Create your models here.

class Student(models.Model):
    full_name = models.CharField(max_length=70)
    
    def _unicode_(self):
        return self.full_name
        
    def _str_(self):
        return self.full_name 

class Request(models.Model):
    date = models.DateField()
    reservation = models.CharField(max_length=70)
    
    
    def _unicode_(self):
        return self.date, self.reservation
        
    def _str_(self):
        return self.date, self.reservation 