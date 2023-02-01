# Generated by Django 4.1.2 on 2023-02-01 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_alter_employee_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(blank=True, choices=[('manager', 'Manager'), ('manager', 'Vice Manager'), ('other_employee', 'Other Employee')], max_length=100, null=True),
        ),
    ]
