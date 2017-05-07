from django.contrib.auth.models import User
from django.db import models


# Customer
class Customer(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    email_address = models.CharField(default='', max_length=250)
    last_name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    is_a_manager = models.BooleanField(default=False)
    department = models.ForeignKey('Department', default=1, on_delete=models.CASCADE)
    customer_order = models.ForeignKey('CustomerOrder', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
       return self.last_name + ' - ' + self.first_name


# CPU
class CPU(models.Model):

   cpu_id = models.CharField(primary_key=True, max_length=100)
   cpu_speed = models.FloatField(default=1,max_length=20)
   cpu_cores = models.IntegerField(default=1)
   cpu_name = models.CharField(max_length=250)
   cpu_price = models.FloatField(max_length=500)
   cpu_manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
   cpu_category = models.ForeignKey('ComponentCategory', on_delete=models.CASCADE)
   cpu_orders = models.ForeignKey('ComponentOrder', on_delete=models.CASCADE)

   def __str__(self):
       return self.cpu_category + self.cpu_name + ' - ' + self.cpu_price


# RAM
class RAM(models.Model):

   ram_id = models.CharField(primary_key=True, max_length=100)
   ram_capacity = models.IntegerField(default=1)
   ram_name = models.CharField(max_length=250)
   ram_price = models.FloatField(max_length=500)
   ram_manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
   ram_category = models.ForeignKey('ComponentCategory', on_delete=models.CASCADE)
   ram_orders = models.ForeignKey('ComponentOrder', on_delete=models.CASCADE)

   def __str__(self):
       return self.ram_category + self.ram_name + ' - ' + self.ram_price


# HDD
class HDD(models.Model):

   hdd_id = models.CharField(primary_key=True, max_length=100)
   hdd_capacity = models.IntegerField(default=1)
   hdd_type = models.CharField(blank=True,max_length=20)
   hdd_name = models.CharField(max_length=250)
   hdd_price = models.FloatField(max_length=500)
   hdd_manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
   hdd_category = models.ForeignKey('ComponentCategory', on_delete=models.CASCADE)
   hdd_orders = models.ForeignKey('ComponentOrder', on_delete=models.CASCADE)

   def __str__(self):
       return self.hdd_category + self.hdd_name + ' - ' + self.hdd_price


# Monitor
class Monitor(models.Model):

   monitor_id = models.CharField(primary_key=True, max_length=100)
   monitor_resolution = models.CharField(blank=True,max_length=250)
   monitor_size = models.FloatField(default=1,max_length=20)
   monitor_name = models.CharField(max_length=250)
   monitor_price = models.FloatField(max_length=500)
   monitor_manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
   monitor_category = models.ForeignKey('ComponentCategory', on_delete=models.CASCADE)
   monitor_orders = models.ForeignKey('ComponentOrder', on_delete=models.CASCADE)

   def __str__(self):
       return self.monitor_category + self.monitor_name + ' - ' + self.monitor_price

# Video Card
class VideoCard(models.Model):
    vc_id = models.CharField(primary_key=True, max_length=100)
    vc_ram = models.IntegerField(default=1)
    vc_clock = models.FloatField(max_length=20)
    vc_name = models.CharField(max_length=250)
    vc_price = models.FloatField(max_length=500)
    vc_manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    vc_category = models.ForeignKey('ComponentCategory', on_delete=models.CASCADE)
    vc_orders = models.ForeignKey('ComponentOrder', on_delete=models.CASCADE)

    def __str__(self):
           return self.vc_category + self.vc_name + ' - ' + self.vc_price

# Power Supply
class PowerSupply(models.Model):

   power_supply_id = models.CharField(primary_key=True, max_length=100)
   power_supply_wattage = models.IntegerField(default=1)
   power_supply_name = models.CharField(max_length=250)
   power_supply_price = models.FloatField(max_length=500)
   power_supply_manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
   power_supply_category = models.ForeignKey('ComponentCategory', on_delete=models.CASCADE)
   power_supply_orders = models.ForeignKey('ComponentOrder', on_delete=models.CASCADE)

   def __str__(self):
       return self.power_supply_category + self.power_supply_name + ' - ' + self.power_supply_price


# Manufacturer
class Manufacturer(models.Model):
   manufacturer_id = models.CharField(primary_key=True, max_length=100)
   manufacturer_name = models.CharField(max_length=250)
   cpu_component_manufacturer = models.ForeignKey('CPU', on_delete=models.CASCADE)
   ram_component_manufacturer = models.ForeignKey('RAM', on_delete=models.CASCADE)
   hdd_component_manufacturer = models.ForeignKey('HDD', on_delete=models.CASCADE)
   monitor_component_manufacturer = models.ForeignKey('Monitor', on_delete=models.CASCADE)
   power_supply_component_manufacturer = models.ForeignKey('PowerSupply', on_delete=models.CASCADE)

   def _str_(self):
       return self.manufacturer_name


# Categories
class ComponentCategory(models.Model):
   category_name = models.CharField(primary_key=True, max_length=100)
   image = models.CharField(max_length=500)

   def __str__(self):
       return self.category_name


# Component Order
class ComponentOrder(models.Model):
   cpu_component_order = models.ForeignKey('CPU', on_delete=models.CASCADE)
   ram_component_order = models.ForeignKey('RAM', on_delete=models.CASCADE)
   hdd_component_order = models.ForeignKey('HDD', on_delete=models.CASCADE)
   monitor_component_order = models.ForeignKey('Monitor', on_delete=models.CASCADE)
   power_supply_component_order = models.ForeignKey('PowerSupply', on_delete=models.CASCADE)
   customer_order_component_order = models.ForeignKey('CustomerOrder', on_delete=models.CASCADE)

   def __str__(self):
       return self.customer_order_component_order


# Customer Order
class CustomerOrder(models.Model):
   order_id = models.IntegerField(blank=True, primary_key=True)
   customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
   order_total = models.FloatField(max_length=250)
   component_order = models.ForeignKey('ComponentOrder', default=1, on_delete=models.CASCADE)

   def __str__(self):
       return self.order_id


# Department
class Department(models.Model):
   department_id = models.IntegerField(blank=True, primary_key=True)
   department_name = models.CharField(max_length=250)

   def __str__(self):
       return self.department_name

