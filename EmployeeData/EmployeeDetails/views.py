from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse
import datetime
from .models import EmployeeData


def get_employee_data(request):
    out=EmployeeData.objects.all()
    return render(request,'employee_data.html',{'data': out})
