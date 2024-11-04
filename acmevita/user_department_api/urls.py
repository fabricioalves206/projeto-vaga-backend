from django.urls import path
from .views import DepartmentListView, EmployeeListView

urlpatterns = [
    path('departments/', DepartmentListView.as_view(), name='department-list'),
    path('departments/<int:department_id>/employees', EmployeeListView.as_view(), name='employee-list'),
]
