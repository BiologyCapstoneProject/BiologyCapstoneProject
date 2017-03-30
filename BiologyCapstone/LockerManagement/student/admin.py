from django.contrib import admin

# Register your models here.

from student.models import Request

class RequestModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Request

admin.site.register(Request, RequestModelAdmin)