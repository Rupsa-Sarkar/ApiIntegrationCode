from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import responses
from rest_framework import status
from .models import Employees
from .serializer import EmployeesSerializer

class Employeelist(APIView):

    def get(self,request):
        employees1 = Employees.objects.all()
        serializer = EmployeesSerializer(employees1,many=True)
        return responses(serializer.data)

    def post(self):
        pass
