from django.contrib import admin
from .models import Customer, Department, ComponentCategory

admin.site.register(Customer)
admin.site.register(Department)
admin.site.register(ComponentCategory)