from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from datetime import datetime

# Create your models here.

class Request(models.Model):
    full_name = models.CharField(max_length=70)
    date = models.CharField(max_length=25, default="Pick a date")
    reservation = models.CharField(max_length=70, default="Reservation")
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def _unicode_(self):
        return self.full_name, self.date, self.reservation, 
        
    def _str_(self):
        return self.full_name, self.date, self.reservation, 