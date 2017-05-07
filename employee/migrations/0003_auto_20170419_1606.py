# Generated by Django 2.0.dev20170411164641 on 2017-04-19 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_customer_is_a_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComponentCategory',
            fields=[
                ('category_id', models.CharField(default=1, max_length=100, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=250)),
                ('image', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ComponentOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('cpu_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('cpu_name', models.CharField(max_length=250)),
                ('cpu_price', models.FloatField(max_length=500)),
                ('cpu_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.ComponentCategory')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerOrder',
            fields=[
                ('order_id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('order_total', models.FloatField(max_length=250)),
                ('component_order', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.ComponentOrder')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='HDD',
            fields=[
                ('hdd_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('hdd_name', models.CharField(max_length=250)),
                ('hdd_price', models.FloatField(max_length=500)),
                ('hdd_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.ComponentCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('manufacturer_id', models.CharField(default=1, max_length=100, primary_key=True, serialize=False)),
                ('manufacturer_name', models.CharField(max_length=250)),
                ('cpu_component_manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.CPU')),
                ('hdd_component_manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.HDD')),
            ],
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('monitor_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('monitor_name', models.CharField(max_length=250)),
                ('monitor_price', models.FloatField(max_length=500)),
                ('monitor_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.ComponentCategory')),
                ('monitor_manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Manufacturer')),
                ('monitor_orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.ComponentOrder')),
            ],
        ),
        migrations.CreateModel(
            name='PowerSupply',
            fields=[
                ('power_supply_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('power_supply_name', models.CharField(max_length=250)),
                ('power_supply_price', models.FloatField(max_length=500)),
                ('power_supply_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.ComponentCategory')),
                ('power_supply_manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Manufacturer')),
                ('power_supply_orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.ComponentOrder')),
            ],
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('ram_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('ram_name', models.CharField(max_length=250)),
                ('ram_price', models.FloatField(max_length=500)),
                ('ram_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.ComponentCategory')),
                ('ram_manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Manufacturer')),
                ('ram_orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.ComponentOrder')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='email_address',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='monitor_component_manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Monitor'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='power_supply_component_manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.PowerSupply'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='ram_component_manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.RAM'),
        ),
        migrations.AddField(
            model_name='hdd',
            name='hdd_manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Manufacturer'),
        ),
        migrations.AddField(
            model_name='hdd',
            name='hdd_orders',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.ComponentOrder'),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='customer_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.Customer'),
        ),
        migrations.AddField(
            model_name='cpu',
            name='cpu_manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Manufacturer'),
        ),
        migrations.AddField(
            model_name='cpu',
            name='cpu_orders',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.ComponentOrder'),
        ),
        migrations.AddField(
            model_name='componentorder',
            name='cpu_component_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.CPU'),
        ),
        migrations.AddField(
            model_name='componentorder',
            name='customer_order_component_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.CustomerOrder'),
        ),
        migrations.AddField(
            model_name='componentorder',
            name='hdd_component_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.HDD'),
        ),
        migrations.AddField(
            model_name='componentorder',
            name='monitor_component_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Monitor'),
        ),
        migrations.AddField(
            model_name='componentorder',
            name='power_supply_component_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.PowerSupply'),
        ),
        migrations.AddField(
            model_name='componentorder',
            name='ram_component_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.RAM'),
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.CustomerOrder'),
        ),
        migrations.AddField(
            model_name='customer',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.Department'),
        ),
    ]
