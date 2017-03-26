from django.contrib import admin

# Register your models here.

from student.models import Student
from student.models import Request

class StudentModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Student

admin.site.register(Student, StudentModelAdmin)

class RequestModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Request

admin.site.register(Request, RequestModelAdmin)