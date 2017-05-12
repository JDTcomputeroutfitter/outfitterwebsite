from django.contrib import admin
from .models import Customer, Department, Manufacturer, ComponentCategory, CPU, RAM, HDD, Monitor, VideoCard, PowerSupply, ComponentOrder, CustomerOrder
admin.site.register(Customer)
admin.site.register(Department)
admin.site.register(Manufacturer)
admin.site.register(ComponentCategory)
admin.site.register(CPU)
admin.site.register(RAM)
admin.site.register(HDD)
admin.site.register(Monitor)
admin.site.register(VideoCard)
admin.site.register(PowerSupply)
admin.site.register(ComponentOrder)
admin.site.register(CustomerOrder)
