# Generated by Django 2.2.20 on 2021-04-11 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210411_1236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.AlterModelTable(
            name='student',
            table='students',
        ),
    ]
