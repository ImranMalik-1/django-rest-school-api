# Generated by Django 3.2.11 on 2022-01-22 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolManagementApp', '0006_alter_school_enrolled_students_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='enrolled_students_count',
        ),
    ]