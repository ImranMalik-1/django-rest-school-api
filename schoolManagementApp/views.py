import logging
import copy 

from django.shortcuts import render
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import login

from rest_framework import status, viewsets, filters, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import ReadOnly

from knox.views import LoginView as KnoxLoginView

from knox.models import AuthToken

from .serializers import SchoolSerializer, StudentSerializer, UserSerializer, RegisterSerializer

from .models import Student, School
from .Util import Util


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['school_name']
    ordering_fields = ['school_name', 'id']
    search_fields = ['school_name', 'id']
    ordering = ['id']
    permission_classes = [IsAuthenticated|ReadOnly]
            

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['first_name']
    search_fields = ['first_name', 'id']
    ordering = ['id']
    permission_classes = [IsAuthenticated|ReadOnly]

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get("school_pk"):
            school_pk = self.kwargs.get("school_pk")
            if not Util.check_if_int(school_pk):
                return Response(dict(status=400, detail='INVALID_SCHOOL_ID'))
            
            school = School.get_by_id(school_pk)
            if school:
                return self.queryset.filter(school=school)
            else:
                raise Http404
        else:
            return self.queryset

    def create(self, request, school_pk=None):
        request_content = copy.deepcopy(request.data)
        if school_pk and not Util.check_if_int(school_pk):
            return Response(dict(status=400, message='INVALID_SCHOOL_ID'))  
        if school_pk:
            request_content['school'] = school_pk        
        serializer = StudentSerializer(data=request_content)
        if serializer.is_valid():
            school_object = School.get_by_id(request_content['school'])
            total_students_in_school = Student.objects.all().filter(school=school_object)
            if len(total_students_in_school) + 1 > school_object.maximum_number_of_students:
                return Response(dict(status=400, detail='MAXIMUM_CAPACITY_REACHED',
                 decription='maximum capacity for school reached, cannot add student'))
            else:
                student_object = serializer.save()
                school_object.enrolled_students_count += 1
                school_object.save()
                return Response(dict(status=201, id=student_object.id))
        else:
            return Response(serializer.errors)
    
    def destroy(self, request, pk=None, school_pk=None):
        if not Util.check_if_int(pk):
            return Response(dict(status=400, detail='INVALID_STUDENT_ID'))
        student = Student.get_by_id(pk)
        if student:
            school_object = student.school
            if school_object:
                school_object.enrolled_students_count -= 1
                school_object.save()
                student.delete()
                return Response(dict(status=200, detail='DELETED'))
            else:
                raise Http404
        else:
            raise Http404
