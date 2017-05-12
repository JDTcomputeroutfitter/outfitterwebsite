from django import forms
from django.contrib.auth.models import User
from employee.models import Customer, Department, CPU, Monitor, RAM, HDD, VideoCard, PowerSupply




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['user', 'last_name', 'first_name', 'department',  'email_address', 'is_a_manager']

    def clean_user(self):
        user = self.cleaned_data.get('user')
        if Customer.objects.filter(user=user).exists():
            raise forms.ValidationError(u'That User already has a customer profile.')
        return user


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_name']

    def clean_department_id(self):
        department_id = self.cleaned_data.get('department_id')
        while True:
            if Department.objects.filter(department_id=department_id).exists():
                department_id += 1
                break
            return department_id


class CPUForm(forms.ModelForm):

    class Meta:
        model = CPU
        fields = ['manufacturer', 'name', 'category', 'cpu_cores', 'cpu_speed', 'price']


class RAMForm(forms.ModelForm):

    class Meta:
        model = RAM
        fields = ['manufacturer', 'name', 'category', 'ram_capacity', 'price']


class HDDForm(forms.ModelForm):

    class Meta:
        model = HDD
        fields = ['manufacturer', 'name', 'category', 'hdd_type', 'hdd_capacity', 'price']


class MonitorForm(forms.ModelForm):

    class Meta:
        model = Monitor
        fields = ['manufacturer', 'name', 'category', 'monitor_size', 'monitor_resolution', 'price']

class VideoCardForm(forms.ModelForm):

    class Meta:
        model = VideoCard
        fields = ['manufacturer', 'name', 'category', 'vc_clock', 'vc_ram', 'price']


class PowerSupplyForm(forms.ModelForm):

    class Meta:
        model = PowerSupply
        fields = ['manufacturer', 'name', 'category', 'power_supply_wattage', 'price']


class ChooseComponentForm(forms.Form):

      fields = forms.ChoiceField(choices=[("cpu","cpu"), ("ram","ram")])



