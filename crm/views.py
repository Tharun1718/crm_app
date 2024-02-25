from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Customer
from .forms import CustomerForm

# Create your views here.
def index(request):
    return render(request, 'crm/index.html',{
        'customers': Customer.objects.all()
    })

def view_customer(request, id):
    customer = Customer.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            new_customer_id = form.cleaned_data['customer_id']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_phone_no = form.cleaned_data['phone_no']
            new_address = form.cleaned_data['address']

        new_customer = Customer(
            customer_id = new_customer_id,
            first_name = new_first_name,
            last_name = new_last_name,
            email = new_email,
            phone_no = new_phone_no,
            address = new_address
        )
        new_customer.save()
        return render(request, 'crm\add.html', {
            'form': CustomerForm(),
            'success': True
        })
    else:
        form = CustomerForm()
    return render(request, 'crm\add.html',{
        'form': CustomerForm()
    })
