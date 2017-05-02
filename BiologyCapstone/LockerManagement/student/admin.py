"""
Register the models in the admin page.
"""

from django.contrib import admin
from student.models import Request

class RequestModelAdmin(admin.ModelAdmin):
    """ list_display shows the fields from the form on the admin page
        search_fields enables the fields for searching on the admin page
    """
    list_display = ('full_name', 'email', 'reservation', 'date', 'true_date', 'timestamp')
    search_fields = ('full_name', 'email', 'reservation', 'date', 'timestamp')

admin.site.register(Request, RequestModelAdmin)