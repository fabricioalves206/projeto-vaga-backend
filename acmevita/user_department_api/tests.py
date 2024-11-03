from django.test import TestCase

from django.test import TestCase
from .models import Department, Employee, Dependent

class DepartmentModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="Desenvolvimento")

    def test_department_creation(self):
        self.assertEqual(self.department.name, "Desenvolvimento")


class EmployeeModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="RH")
        self.employee = Employee.objects.create(full_name="João Silva", department=self.department)

    def test_employee_have_dependents(self):
        self.assertFalse(self.employee.have_dependents)

class DependentModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="Desenvolvimento")
        self.employee = Employee.objects.create(full_name="Maicon Jequison", department=self.department)
        self.dependent = Dependent.objects.create(name="Maicon Jequison Junior", employee=self.employee)
    
    def test_employee_have_dependents(self):
        self.assertTrue(self.employee.have_dependents)
