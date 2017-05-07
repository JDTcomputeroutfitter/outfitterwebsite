from django import forms
from django.contrib.auth.models import User
from employee.models import Customer, Department





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



