from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        widgets = {
                    'client': forms.Select(attrs={
                        'class': 'border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
                    }),
                    'freelancer': forms.Select(attrs={
                        'class': 'border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
                    }),
                    'description': forms.Textarea(attrs={
                        'class': 'border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                        'placeholder': 'Enter invoice description',
                        'rows': 4
                    }),
                    'amount': forms.NumberInput(attrs={
                        'class': 'border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                        'placeholder': 'Enter invoice amount'
                    }),
                    'issue_date': forms.DateInput(attrs={
                        'class': 'border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                        'type': 'date'
                    }),
                    'due_date': forms.DateInput(attrs={
                        'class': 'border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                        'type': 'date'
                    }),
                    'status': forms.Select(attrs={
                        'class': 'border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
                    }),
                }





    
    issue_date = forms.DateField(input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'type': "date"}))

    due_date = forms.DateField(input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'type': "date"}))

          