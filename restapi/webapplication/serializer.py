from rest_framework import serializers
from rest_framework import Employees

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        #fields=('firstname','lastname')
        fields='__all__'