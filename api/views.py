from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from api.models import Student
from api.serializers import StudentSerializer

# Create your views here.


class StudentsView(ModelViewSet):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    model=Student