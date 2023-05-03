from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Employee, Department
from .forms import EmployeeForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 

def index(request):
    departments = Department.objects.all() 
    context = { 'departments': departments }
    return render(request, 'employee_register/index.html', context)

def read_more(request):
    return render(request, 'employee_register/read_more.html')

def employee_list(request):
    employees = Employee.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(employees, 10) # show 5 employees per page
     
    try:
        emps = paginator.page(page)
    except PageNotAnInteger:
        emps = paginator.page(1)
    except EmptyPage:
        emps = paginator.page(paginator.num_pages)
    return render(request, 'employee_register/employee_list.html', {'emps': emps})

    
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    context = { 'employee': employee }
    return render(request, 'employee_register/employee_detail.html', context)

@login_required(login_url='login')
def add_employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/employee_register/')
    return render(request, 'employee_register/employee_form.html', {'form': form})

@login_required(login_url='login')
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/employee_register/')
    return render(request, 'employee_register/employee_form.html', {'form': form})
    
def department_list(request):
    departments = Department.objects.all() 
    context = { 'departments': departments }
    return render(request, 'employee_register/department_list.html', context)
    
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk) 
    context = { 'department': department } 
    return render(request, 'employee_register/department_detail.html', context)

@login_required(login_url='login')
def delete_employee(request, pk):
    x = Employee.objects.get(pk=pk)
    x.delete()
    return redirect("/employee_register/")








