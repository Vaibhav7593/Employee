
from django import forms
from EmpApp.models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model= Employee
        fields= "__all__"

class UpdateEmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

        labels={
            'Name': 'Updated Name',
            'Salary':'Updated Salary',
            'Emp_ID':'Updated Employee ID'
        }

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

