from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from fbvApp.models import Student
from fbvApp.serializers import StudentSerializer


class StudentPagination(LimitOffsetPagination):
    default_limit = 4

class StudentViewSet(viewsets.ModelViewSet):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentPagination

"""
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
"""