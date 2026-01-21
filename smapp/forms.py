from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'firstname', 'lastname', 'age', 'email', 'phone',
            'staffID', 'title', 'position', 'department',
            'division', 'unit', 'start_date'
        ]
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'First Name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Last Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Age'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Phone'}),
            'staffID': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'StaffID'}),
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Title'}),
            'position': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Position'}),
            'department': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Department'}),
            'division': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Division'}),
            'unit': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Unit'}),
            'start_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
        }