def department_serializer(department):
    return {"pk": department.id, "name": department.name}

def employee_serializer(employee):
    return {"full_name": employee.full_name, "have_dependent": employee.dependents.exists()}
