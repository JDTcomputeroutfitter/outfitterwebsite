from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, ComponentCategory, CPU, RAM, HDD, Monitor, VideoCard, PowerSupply, ComponentOrder, CustomerOrder
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import UserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import View
from django.contrib.auth.models import User


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


#def asddff(request, category_name_id):
  #  if not request.user.is_authenticated():
   ##else:
     #   category = get_object_or_404(ComponentCategory, pk=category_name_id)
      #  return render(request, 'employee/templates/components.html', {'category': category})

def category_index(request):
   if not request.user.is_authenticated:
       return render(request, 'employee/templates/login.html')
   else:
       user = request.user
       categories = ComponentCategory.objects.all()
       cpu_results = CPU.objects.all()
       ram_results = RAM.objects.all()
       hdd_results = HDD.objects.all()
       monitor_results = Monitor.objects.all()
       videocard_results = VideoCard.objects.all()
       powersupply_results = PowerSupply.objects.all()
       return render(request, 'employee/templates/components.html', {
           'categories': categories,
           'cpu': cpu_results,
           'ram': ram_results,
           'hdd': hdd_results,
           'monitor': monitor_results,
           'videocard': videocard_results,
           'powersupply': powersupply_results,
           'user': user,
           })


def cpu_order(request, cpu_id):
   cpu = get_object_or_404(CPU, pk=cpu_id)
   categories = ComponentCategory.objects.all()
   cpu_results = CPU.objects.all()
   ram_results = RAM.objects.all()
   hdd_results = HDD.objects.all()
   monitor_results = Monitor.objects.all()
   videocard_results = VideoCard.objects.all()
   powersupply_results = PowerSupply.objects.all()
   try:
       if cpu.ordered:
           cpu.ordered = False
       else:
           CPU.objects.all().update(ordered = False)
           cpu.ordered = True
       cpu.save()
   except (KeyError, CPU.DoesNotExist):
       return JsonResponse({'success': False})
   else:
       return render(request, 'employee/templates/components.html', {
           'categories': categories,
           'cpu': cpu_results,
           'ram': ram_results,
           'hdd': hdd_results,
           'monitor': monitor_results,
           'videocard': videocard_results,
           'powersupply': powersupply_results,
           })

def ram_order(request, ram_id):
   ram = get_object_or_404(RAM, pk =ram_id )
   categories = ComponentCategory.objects.all()
   cpu_results = CPU.objects.all()
   ram_results = RAM.objects.all()
   hdd_results = HDD.objects.all()
   monitor_results = Monitor.objects.all()
   videocard_results = VideoCard.objects.all()
   powersupply_results = PowerSupply.objects.all()
   try:
       if ram.ordered:
           ram.ordered = False
       else:
           RAM.objects.all().update(ordered = False)
           ram.ordered = True
       ram.save()
   except (KeyError, RAM.DoesNotExist):
       return JsonResponse({'success': False})
   else:
       return render(request, 'employee/templates/components.html', {
           'categories': categories,
           'cpu': cpu_results,
           'ram': ram_results,
           'hdd': hdd_results,
           'monitor': monitor_results,
           'videocard': videocard_results,
           'powersupply': powersupply_results,
           })


def hdd_order(request, hdd_id):
   hdd = get_object_or_404(HDD, pk=hdd_id)
   categories = ComponentCategory.objects.all()
   cpu_results = CPU.objects.all()
   ram_results = RAM.objects.all()
   hdd_results = HDD.objects.all()
   monitor_results = Monitor.objects.all()
   videocard_results = VideoCard.objects.all()
   powersupply_results = PowerSupply.objects.all()
   try:
       if hdd.ordered:
           hdd.ordered = False
       else:
           hdd.ordered = True
       hdd.save()
   except (KeyError, HDD.DoesNotExist):
       return JsonResponse({'success': False})
   else:
       return render(request, 'employee/templates/components.html', {
           'categories': categories,
           'cpu': cpu_results,
           'ram': ram_results,
           'hdd': hdd_results,
           'monitor': monitor_results,
           'videocard': videocard_results,
           'powersupply': powersupply_results,
           })


def monitor_order(request, monitor_id):
   monitor = get_object_or_404(Monitor, pk=monitor_id)
   categories = ComponentCategory.objects.all()
   cpu_results = CPU.objects.all()
   ram_results = RAM.objects.all()
   hdd_results = HDD.objects.all()
   monitor_results = Monitor.objects.all()
   videocard_results = VideoCard.objects.all()
   powersupply_results = PowerSupply.objects.all()
   try:
       if monitor.ordered:
           monitor.ordered = False
       else:
           Monitor.objects.all().update(ordered = False)
           monitor.ordered = True
       monitor.save()
   except (KeyError, Monitor.DoesNotExist):
       return JsonResponse({'success': False})
   else:
       return render(request, 'employee/templates/components.html', {
           'categories': categories,
           'cpu': cpu_results,
           'ram': ram_results,
           'hdd': hdd_results,
           'monitor': monitor_results,
           'videocard': videocard_results,
           'powersupply': powersupply_results,
           })


def videocard_order(request, videocard_id):
   videocard = get_object_or_404(VideoCard, pk=videocard_id)
   categories = ComponentCategory.objects.all()
   cpu_results = CPU.objects.all()
   ram_results = RAM.objects.all()
   hdd_results = HDD.objects.all()
   monitor_results = Monitor.objects.all()
   videocard_results = VideoCard.objects.all()
   powersupply_results = PowerSupply.objects.all()
   try:
       if videocard.ordered:
           videocard.ordered = False
       else:
           VideoCard.objects.all().update(ordered = False)
           videocard.ordered = True
       videocard.save()
   except (KeyError, VideoCard.DoesNotExist):
       return JsonResponse({'success': False})
   else:
       return render(request, 'employee/templates/components.html', {
           'categories': categories,
           'cpu': cpu_results,
           'ram': ram_results,
           'hdd': hdd_results,
           'monitor': monitor_results,
           'videocard': videocard_results,
           'powersupply': powersupply_results,
           })


def powersupply_order(request, powersupply_id):
   powersupply = get_object_or_404(PowerSupply, pk=powersupply_id)
   categories = ComponentCategory.objects.all()
   cpu_results = CPU.objects.all()
   ram_results = RAM.objects.all()
   hdd_results = HDD.objects.all()
   monitor_results = Monitor.objects.all()
   videocard_results = VideoCard.objects.all()
   powersupply_results = PowerSupply.objects.all()
   try:
       if powersupply.ordered:
           powersupply.ordered = False
       else:
           PowerSupply.objects.all().update(ordered = False)
           powersupply.ordered = True
       powersupply.save()
   except (KeyError, PowerSupply.DoesNotExist):
       return JsonResponse({'success': False})
   else:
       return render(request, 'employee/templates/components.html', {
           'categories': categories,
           'cpu': cpu_results,
           'ram': ram_results,
           'hdd': hdd_results,
           'monitor': monitor_results,
           'videocard': videocard_results,
           'powersupply': powersupply_results,
           })
