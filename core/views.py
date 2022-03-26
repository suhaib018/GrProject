from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.


def index(request):
    facility = Faculty.objects.get(id=1 )
    employees=Employee.objects.filter(department_employees__faculty_id=facility.id)
    return render(request,'index.html',{'emps':employees})
    