# Generated by Django 3.1.7 on 2021-03-23 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolManagement', '0003_teacher_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='fcm_token',
        ),
    ]
