from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields= ['customer_id','first_name','last_name','email','phone_no','address']
        labels = {
            'customer_id': 'Customer Id',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone_no': 'Phone Number',
            'address': 'Address'
        }
        widgets = {
            'customer_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'})
        }