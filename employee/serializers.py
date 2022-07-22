from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    department = serializers.CharField(source='department.name')
    class Meta:
        model = Employee
        fields =['name', 'email', 'department']