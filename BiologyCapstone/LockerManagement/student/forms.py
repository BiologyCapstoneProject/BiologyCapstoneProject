""" Connects the interface to the models.
"""

from django import forms
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model= Request
        fields= ['full_name', 'date', 'reservation', 'email', 'phone_num']
    
    """ Below is the email functionallity, 
        we did not obtain an email address 
        that had security features that enables
        mass emails. 
    """
        
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     email_base, provider = email.split("@")
    #     domain, extension = provider.split('.')
    #     if not domain == 'rollins':
    #         raise forms.ValidationError("Please make sure to enter a Rollins email")
    #     if not extension == "edu":
    #         raise forms.ValidationError("Please use a valid .EDU email address")
    #     return email
    # def clean_name(self):
    #     full_name = self.clened_data.get('full_name')
    #     raise forms.ValidationError("Please enter your name")
    #     return full_name