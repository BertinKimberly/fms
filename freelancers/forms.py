from django import forms
from .models import Freelancer

class FreelancerForm(forms.ModelForm):
    class Meta:
        model = Freelancer
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter client name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter client name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter client email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter phone number'
            }),
            'skills': forms.Textarea(attrs={
                'class': 'border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter client address',
                'rows': 4
            }),
             'hourly_rate': forms.NumberInput(attrs={
                'class': 'border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter Hourly Rate'
            }),
        }