# Generated by Django 4.2.1 on 2023-06-01 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=16)),
                ('last_name', models.CharField(max_length=16)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_number', models.CharField(max_length=12)),
                ('department_id', models.BigIntegerField(blank=True)),
                ('department', models.CharField(blank=True, max_length=50)),
                ('start_time', models.TimeField(auto_now_add=True)),
                ('leaves', models.IntegerField(default=18)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday_title', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'holidays',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=32)),
                ('skill_type', models.CharField(max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'skills',
            },
        ),
        migrations.CreateModel(
            name='EmployeeFinance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('benevolent', models.FloatField(default=2.5)),
                ('fuel_allowance', models.IntegerField(default=3000)),
                ('special_allowance', models.IntegerField(default=0)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='employees.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True)),
                ('cnic', models.CharField(blank=True, max_length=16)),
                ('joining_date', models.DateField(blank=True)),
                ('contact_number', models.CharField(max_length=12)),
                ('salary', models.IntegerField()),
                ('job_status', models.CharField(choices=[('intern', 'Internee'), ('irobation', 'Probation Period'), ('onboard', 'Onboard'), ('notice', 'Notice Period')], max_length=32)),
                ('role', models.CharField(blank=True, max_length=50)),
                ('designation', models.CharField(blank=True, max_length=50)),
                ('bank_name', models.CharField(blank=True)),
                ('bank_account_number', models.IntegerField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='employees.employee')),
            ],
            options={
                'db_table': 'employee_details',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='2023-06-01')),
                ('check_in', models.TimeField()),
                ('check_out', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
            ],
            options={
                'db_table': 'check_ins',
            },
        ),
    ]