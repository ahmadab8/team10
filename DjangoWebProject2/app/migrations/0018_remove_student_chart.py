# Generated by Django 2.2.20 on 2021-04-29 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_student_chart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='chart',
        ),
    ]
