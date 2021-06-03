# Generated by Django 2.2.23 on 2021-06-03 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_merge_20210603_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('M', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'aboutmss',
            },
        ),
        migrations.AlterField(
            model_name='tutor',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name=''),
        ),
    ]
