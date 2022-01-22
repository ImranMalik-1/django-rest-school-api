import uuid
from datetime import datetime    

from django.db import models


class School(models.Model):
    created = models.DateTimeField(editable=False, auto_now_add=True)
    updated = models.DateTimeField(editable=False, auto_now=True)
    school_name = models.CharField(max_length=20)
    maximum_number_of_students = models.IntegerField(default=50)

    def __str__(self):
        return self.school_name
    
    @classmethod
    def get_id(self):
        return self.id
    
    @classmethod
    def get_by_id(self, id):
        try:
            school = School.objects.get(pk=id)
            return school
        except School.DoesNotExist:
            return None


class Student(models.Model):
    created = models.DateTimeField(editable=False, auto_now_add=True)
    updated = models.DateTimeField(editable=False, auto_now=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_id
    
    @classmethod
    def get_id(self):
        return self.id
    
    @classmethod
    def get_by_id(self, id):
        try:
            student = Student.objects.get(pk=id)
            return student
        except Student.DoesNotExist:
            return None

