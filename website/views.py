from django.shortcuts import render
from employee.models import Employee
from department.models import Department

# Create your views here.
0
def index (request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    context = {
        "employees": employees,
        "departments": departments
    }
    return render(request, "index.html", context)
