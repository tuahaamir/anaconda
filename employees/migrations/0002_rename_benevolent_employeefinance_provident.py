# Generated by Django 4.2.1 on 2023-06-01 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeefinance',
            old_name='benevolent',
            new_name='provident',
        ),
    ]
