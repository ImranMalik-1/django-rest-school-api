from django.contrib import admin

# Register your models here.

from .models import Student
from .models import School

admin.site.register(School)
admin.site.register(Student)