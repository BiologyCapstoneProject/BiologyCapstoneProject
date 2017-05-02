""" Creates model objects.
"""

from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django.utils import timezone
from django.contrib import admin

class Request(models.Model):
    """ Creates the request table with
        full name, date, reservation, email address,
        phone number, and a timestamp. 
    """
    full_name = models.CharField(max_length=70, default="Full Name")
    date = models.CharField(max_length=25, default="Pick a date")
    reservation = models.CharField(max_length=70, default="Reservation")
    email = models.CharField(max_length=70, default="Email")
    phone_num = models.CharField(max_length=10, default="Phone ")
    true_date = models.DateTimeField(default=datetime.now() , editable=True)
    timestamp = models.DateTimeField(default=datetime.now() , editable=True)
    
    
    