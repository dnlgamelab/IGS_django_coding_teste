from rest_framework import serializers
from .models import Employee

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields =['name' 'email', 'department']