from django.urls import path
from .views import departments_list, employees_by_department_list

urlpatterns = [
    path('departments/', departments_list, name='department-list'),
    path('departments/<int:department_id>/employees', employees_by_department_list, name='employee-list'),
]
