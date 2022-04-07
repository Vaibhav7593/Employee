from django.shortcuts import redirect, render

from EmpApp.forms import AddEmployeeForm, RegistrationForm, UpdateEmployeeForm
from EmpApp.models import Employee
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'EmpApp/home.html')

@login_required
def add_employee(request):
    form= AddEmployeeForm()
    print(request.POST)
    
    if request.method == "POST":
        form =AddEmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/emp/list/')
    
    return render(request, 'EmpApp/add.html',{'form':form})

@login_required
def list_emp(request):
    data=Employee.objects.all()
    return render(request,'EmpApp/list.html',{'data': data})

@login_required
def emp_detail(request,id):
    data=Employee.objects.get(pk=id)
    return render(request,'EmpApp/detail.html',{'data':data})

@login_required
def emp_update(request,id):
    data=Employee.objects.get(pk=id)
    form= UpdateEmployeeForm(instance=data)
    
    if request.method == "POST":
        form =UpdateEmployeeForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect(f'/emp/detail/{data.id}')
    
    return render(request,'EmpApp/update.html',{'form':form,'data':data})

@login_required
def emp_delete(request,id):
    data=Employee.objects.get(pk=id)
    data.delete()
    return redirect('/emp/list/')


def register_view(request):
    form=RegistrationForm()

    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/emp/home/')
            

    return render(request,'EmpApp/register.html',{'form':form})
