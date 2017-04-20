from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Request(models.Model):
    full_name = models.CharField(max_length=70, default="Full Name")
    date = models.CharField(max_length=25, default="Pick a date")
    reservation = models.CharField(max_length=70, default="Reservation")
    email = models.CharField(max_length=70, default="Email")
    phone_num = models.CharField(max_length=10, default="Phone ")
    timestamp = models.DateTimeField(default=datetime.now() , editable=True)
    
    class meta:
        verbose_name= "full name",
    def _unicode_(self):
        return self.full_name,self.date, self.reservation, self.timestamp,
        
    # def _str_(self):
    #     return self.full_name, self.date, self.reservation, self.timestamp,
    
class RequestAdmin(models.AdminModel):
    def request(self, obj) :
         """My Custom Title"""
    ...
    my_function.short_description = 'full_e'