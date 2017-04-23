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
    
    
    