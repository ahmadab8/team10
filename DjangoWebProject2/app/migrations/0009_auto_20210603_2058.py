# Generated by Django 2.2.23 on 2021-06-03 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210603_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmss',
            name='M',
            field=models.CharField(max_length=1000),
        ),
    ]
