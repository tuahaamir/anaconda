from calendar import monthrange
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . import models
from django.db.models import Q
import numpy as np
from datetime import datetime
from django.forms import model_to_dict
import requests
from num2words import num2words



def hello(request):
    return HttpResponse("You're looking at question.")


def absent(request):
    absents = models.Attendance.objects.filter(employee=4).all()
    return HttpResponse(absents)


def attendences(request):
    attendances = models.Attendance.objects.filter(Q(employee__id=1) & Q(date__month=4))
    # Extract desired columns or attributes from the queryset
    attendance_data = [
        {
            "employee": attendance.employee.first_name
            + " "
            + attendance.employee.last_name,
            "check_in": attendance.check_in,
            "check_out": attendance.check_out,
            "created_at": attendance.created_at,
            "updated_at": attendance.updated_at,
        }
        for attendance in attendances
    ]

    context = {"attendances": attendance_data}

    return render(request, "attendances.html", context)


def count_attendance(request):
    employee_id = request.GET.get('employee_id')
    month = request.GET.get('month')
    
    attendances = models.Attendance.objects.filter(Q(employee__id=employee_id) & Q(date__month=month))
    holidays = models.Holiday.objects.filter(date__month=month)
    start_date = datetime.strptime(f"2023-{month}-01", "%Y-%m-%d")
    end_date = start_date.replace(day=1, month=start_date.month + 1) if start_date.month < 12 else start_date.replace(day=1, month=1, year=start_date.year + 1)
    
    working_days = np.busday_count(start_date.date(), end_date.date())
    attendances_count = len(attendances)
    
    finance = models.EmployeeFinance.objects.filter(employee_id=employee_id).select_related('employee').first()
    days_in_month = monthrange(2023,5)[1]
    
    holly_dates = []
    for holliday in holidays:
        holly_dates.append(holliday.date)
    
    overtime = 0
    for attendance in attendances:
        if attendance.date in holly_dates or attendance.date.weekday() in [5, 6]:
            overtime += 1
    
    total_salary = finance.salary + finance.fuel_allowance + finance.special_allowance
    provident_fund = finance.salary/100 * finance.provident
    net_salary = total_salary - provident_fund
    
    data = {
        "calender": {
            "days_in_month": days_in_month,
            "working_days": int(working_days),
            "holidays": len(holidays), 
            "attendances": attendances_count,
            "overtime": overtime,
        },
        "finance": {
            "employee_name": finance.employee.first_name + " " + finance.employee.last_name,
            "salary": finance.salary,
            "provident": provident_fund,
            "fuel_allowance": finance.fuel_allowance,
            "special_allowance": finance.special_allowance,
            "total_salary": total_salary,
            "net_salary": net_salary,
            "salary_in_words": num2words(net_salary, to = 'currency')
        }
    }
    
    return JsonResponse(data)


def slip(request):
    employee_id = 4  # Replace with the actual employee ID
    month = 4  # Replace with the actual month (e.g., May)

    # Make a GET request to count_attendance URL and pass the employee_id and month as query parameters
    response = requests.get(f"{request.scheme}://{request.get_host()}/front/count", params={'employee_id': employee_id, 'month': month})
    attendance_data = response.json()

    return render(request, "slipp.html", {'attendance_data': attendance_data})