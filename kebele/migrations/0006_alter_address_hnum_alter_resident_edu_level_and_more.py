# Generated by Django 4.1.2 on 2023-02-09 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kebele', '0005_alter_birthcertificate_father_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='hnum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kebele.house'),
        ),
        migrations.AlterField(
            model_name='resident',
            name='edu_level',
            field=models.CharField(blank=True, choices=[('elementary', 'Elementary'), ('hight_school', 'High School'), ('diploma', 'Diploma'), ('degree', 'Degree'), ('masters', 'Masters'), ('phd', 'PHD')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='resident',
            name='occupation',
            field=models.CharField(blank=True, choices=[('teacher', 'Teacher'), ('merchant', 'Merchant'), ('office_worker', 'Office Worker'), ('nurse', 'Nurse'), ('doctor', 'Doctor'), ('student', 'Student'), ('other', 'Other'), ('none', 'None')], max_length=100, null=True),
        ),
    ]