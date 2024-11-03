from django.db import models

class Department(models.Model):
    """model for departments from ACMEVita"""
    name = models.CharField(max_length=100, unique=True, db_index=True)


class Employee(models.Model):
    """model for employees from ACMEVita"""

    full_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL, related_name="employees")

    @property
    def have_dependents(self):
        return self.dependents.exists()
    

class Dependent(models.Model):
    """model for employee dependents"""
    
    name = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="dependents")