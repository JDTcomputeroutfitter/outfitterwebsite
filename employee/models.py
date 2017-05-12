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
    cpu_speed = models.FloatField(default=1,max_length=20)
    cpu_cores = models.IntegerField(default=1)
    name = models.CharField(max_length=250)
    price = models.FloatField(max_length=500)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    category = models.ForeignKey('ComponentCategory', on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    cpu_orders = models.ForeignKey('CustomerOrder',blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + str(self.price)


# RAM
class RAM(models.Model):
    ram_capacity = models.IntegerField(default=1)
    name = models.CharField(max_length=250)
    price = models.FloatField(max_length=500)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    category = models.ForeignKey('ComponentCategory', on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    ram_orders = models.ForeignKey('CustomerOrder', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + str(self.price)


# HDD
class HDD(models.Model):
    hdd_capacity = models.IntegerField(default=1)
    hdd_type = models.CharField(blank=True,max_length=20)
    name = models.CharField(max_length=250)
    price = models.FloatField(max_length=500)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    category = models.ForeignKey('ComponentCategory', on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    hdd_orders = models.ForeignKey('CustomerOrder', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + str(self.price)


# Monitor
class Monitor(models.Model):
    monitor_resolution = models.CharField(blank=True,max_length=250)
    monitor_size = models.FloatField(default=1,max_length=20)
    name = models.CharField(max_length=250)
    price = models.FloatField(max_length=500)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    category = models.ForeignKey('ComponentCategory', on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    monitor_orders = models.ForeignKey('CustomerOrder', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + str(self.price)


# Video Card
class VideoCard(models.Model):
    vc_ram = models.IntegerField(default=1)
    vc_clock = models.FloatField(max_length=20)
    name = models.CharField(max_length=250)
    price = models.FloatField(max_length=500)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    category = models.ForeignKey('ComponentCategory', on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    vc_orders = models.ForeignKey('CustomerOrder', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + str(self.price)


# Power Supply
class PowerSupply(models.Model):
    power_supply_wattage = models.IntegerField(default=1)
    name = models.CharField(max_length=250)
    price = models.FloatField(max_length=500)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    category = models.ForeignKey('ComponentCategory', on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    power_supply_orders = models.ForeignKey('CustomerOrder', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + str(self.price)


# Manufacturer
class Manufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True, max_length=100)
    manufacturer_name = models.CharField(max_length=250)

    def __str__(self):
        return self.manufacturer_name


# Categories
class ComponentCategory(models.Model):
    category_name = models.CharField(primary_key=True, max_length=100)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.category_name


#Component Order
class ComponentOrder(models.Model):
    CPU = models.ForeignKey('CPU', on_delete=models.CASCADE)
    RAM = models.ForeignKey('RAM', on_delete=models.CASCADE)
    HDD = models.ForeignKey('HDD', on_delete=models.CASCADE)
    Video_Card = models.ForeignKey('VideoCard', on_delete=models.CASCADE)
    Monitor = models.ForeignKey('Monitor', on_delete=models.CASCADE)
    Power_Supply = models.ForeignKey('PowerSupply', on_delete=models.CASCADE)
    component_order = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.component_order)


# Customer Order
class CustomerOrder(models.Model):
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
    order_total = models.FloatField(max_length=250)
    component_order = models.ForeignKey('ComponentOrder', default=1, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.component_order)


# Department
class Department(models.Model):
    department_id = models.AutoField(blank=True, primary_key=True)
    department_name = models.CharField(max_length=250)

    def __str__(self):
        return self.department_name
