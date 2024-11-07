from django.http import JsonResponse
from .models import Department, Employee
from .serializers import department_serializer, employee_serializer

def departments_list(request):
    departments = Department.objects.all()
    data = [department_serializer(department) for department in departments]
    return JsonResponse(data, safe=False)


def employees_by_department_list(request, department_id):
    try:
        department = Department.objects.get(id=department_id)
    except Department.DoesNotExist:
        return JsonResponse({"error": "Department Not Found."}, status=404)

    employees = department.employees.all()
    data = [employee_serializer(employee) for employee in employees]
    return JsonResponse(data, safe=False)
