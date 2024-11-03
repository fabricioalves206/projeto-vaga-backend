from rest_framework import generics
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer

class DepartmentListView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        department_id = self.kwargs['department_id']
        return Employee.objects.filter(department__id=department_id)
