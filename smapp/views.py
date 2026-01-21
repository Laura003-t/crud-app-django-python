from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import EmployeeForm
from django.contrib.auth.models import User
from django.db import models

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('employee_list')

    else:
        form = AuthenticationForm()
    return render(request, 'hrapp/login.html', {'form': form})

@login_required
def employee_list(request):
    employees = Employee.objects.all()

    #Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        employees = employees.filter(
            models.Q(firstname__icontains=search_query) |
            models.Q(lastname__icontains=search_query) |
            models.Q(staffID__icontains=search_query) |
            models.Q(department__icontains=search_query)
        )

    context = {
        'employees': employees,
        'search_query': search_query
    }
    return render(request, 'hrapp/employee_list.html', context)

@login_required
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.added_by = request.user
            employee.save()
            messages.success(request, f'Employee {employee.fullname} added successfully!')
            return redirect('employee_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EmployeeForm()

    return render(request, 'hrapp/employee_form.html', {'form': form, 'action': 'Add'})

@login_required
def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, f'Employee {employee.fullname} updated successfully!')
            return redirect('employee_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'hrapp/employee_form.html', {'form': form, 'action': 'Edit', 'employee': employee})

@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'hrapp/employee_detail.html', {'employee': employee})

@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        employee_name = employee.fullname
        employee.delete()
        messages.success(request, f'Employee {employee_name} deleted successfully!')
        return redirect('employee_list')

    return render(request, 'hrapp/employee_confirm_delete.html', {'employee': employee})