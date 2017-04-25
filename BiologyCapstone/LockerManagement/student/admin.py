from django.contrib import admin

# Register your models here.

from student.models import Request

class RequestModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'reservation', 'date', 'timestamp')
    search_fields = ('full_name', 'email', 'reservation', 'date', 'timestamp')

admin.site.register(Request, RequestModelAdmin)