from django.shortcuts import render, get_object_or_404, redirect
from employee.models import Customer, Department
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from employee.forms import UserForm
from manager.forms import CustomerForm, DepartmentForm
from django.contrib.auth.models import User
from django.db.models import Q


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'employee/templates/login.html')
    else:
        customers = Customer.objects.filter(user=request.user)
        return render(request, 'manager/templates/index.html', {'customers': customers})


def customer_details(request, user):
    if not request.user.is_authenticated :

        return render(request, 'manager/templates/login.html')
    else:
        customer = get_object_or_404(Customer, pk=user)
        return render(request, 'manager/templates/customer_details.html', {'customer': customer, 'user': user})

def customer_index(request):
    if not request.user.is_authenticated:
        return render(request, 'manager/templates/login.html')
    else:
        departments = Department.objects.all()
        customers = Customer.objects.all()
        if request.method == "POST":
            department = request.POST['department']
            try:
                department_id=get_object_or_404(Department, department_name=department)
            except:
                return render(request, 'manager/templates/customer_index.html', {'customers': customers, 'departments':departments})
            customers = Customer.objects.filter(department=department_id)
       
        query = request.GET.get("q")
        if query:
            customers = customers.filter(
                Q(customer_last_name_icontains=query) |
                Q(customer_first_name__icontains=query)
            ).distinct()
            return render(request, 'manager/templates/customer_index.html', {
                          'customers': customers, 'departments':departments,})
        else:
            return render(request, 'manager/templates/customer_index.html', {'customers': customers,'departments':departments,})


def register(request):
    if not request.user.is_authenticated:
        return render(request, 'employee/templates/login.html')
    else:
        form = UserForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('manager:register')
        else:
            context = {
                "form": form,
            }

            return render(request, 'manager/templates/register.html', context)


def register_customer(request):
    if not request.user.is_authenticated:
        return render(request, 'manager/templates/login.html')
    else:
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('manager:register_customer')
        else:
            context = {
                "form": form,
            }
            return render(request, 'manager/templates/register_customer.html', context)

def register_department(request):
    if not request.user.is_authenticated:
        return render(request, 'manager/templates/login.html')
    else:
        form = DepartmentForm(request.POST or None)
        if form.is_valid():
            department = form.save(commit=False)
            department.save()
            return render(request, 'manager/templates/index.html', {'department': department})
        context = {
            "form": form,
        }
        return render(request, 'manager/templates/register_department.html', context)


def change_password(request):
    if not request.user.is_authenticated:
        return render(request, 'manager/templates/login.html')
    else:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                return redirect('manager:manager_profile')

        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'manager/templates/change_password.html', {
            'form': form
        })

def manager_profile(request):
    if not request.user.is_authenticated:
        return render(request, 'manager/templates/login.html')
    else:
        customer = get_object_or_404(Customer, user=request.user)
        return render(request, 'manager/templates/manager_profile.html', {'customer': customer})
