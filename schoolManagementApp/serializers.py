import logging

from rest_framework import serializers
from django.contrib.auth.models import User

from .models import School, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'school_name', 'maximum_number_of_students']
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'student_id', 'school', 'id')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
