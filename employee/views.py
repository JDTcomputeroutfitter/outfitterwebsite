from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import UserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash



def index(request):
    if not request.user.is_authenticated:
        return render(request, 'employee/templates/login.html')
    else:
        customers = Customer.objects.filter(user=request.user)
        return render(request, 'employee/templates/index.html', {'customers': customers})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'employee/templates/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                try:
                    customers = Customer.objects.filter(user=request.user)
                    customer = get_object_or_404(Customer, user = request.user)
                except:
                    return render(request, 'employee/templates/no_customer_account.html')
                if customer.is_a_manager:
                    return render(request, 'manager/templates/index.html', {'customers': customers})
                else:
                    return render(request, 'employee/templates/index.html', {'customers': customers})

            else:
                return render(request, 'employee/templates/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'employee/templates/login.html', {'error_message': 'Invalid login'})

    return render(request, 'employee/templates/login.html')

def change_password(request):
    if not request.user.is_authenticated:
        return render(request, 'employee/templates/login.html')
    else:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                return redirect('employee:employee_profile')

        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'employee/templates/change_password.html', {'form': form})

def employee_profile(request):
    if not request.user.is_authenticated:
        return render(request, 'employee/templates/login.html')
    else:
        customer = get_object_or_404(Customer, user=request.user)
        return render(request, 'employee/templates/employee_profile.html', {'customer': customer})

#below was code to register a person who didnt have an account on the base visitor nav bar
#def register(request):
#    form = UserForm(request.POST or None)
#    if form.is_valid():
#        user = form.save(commit=False)
#        username = form.cleaned_data['username']
#        password = form.cleaned_data['password']
#        user.set_password(password)
#        user.save()
#        user = authenticate(username=username, password=password)
#        if user is not None:
#            if user.is_active:
#                login(request, user)
#                customers = Customer.objects.filter(user=request.user)
#                return render(request, 'employee/templates/index.html', {'customers': customers})
#    context = {
#        "form": form,
#    }
#    return render(request, 'employee/templates/register.html', context)
