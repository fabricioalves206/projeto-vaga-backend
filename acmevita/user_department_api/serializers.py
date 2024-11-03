from rest_framework import serializers
from .models import Department, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name']


class EmployeeSerializer(serializers.ModelSerializer):
    have_dependents = serializers.BooleanField()

    class Meta:
        model = Employee
        fields = ['full_name', 'have_dependents']