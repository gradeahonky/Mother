# Generated by Django 2.0.2 on 2018-11-13 00:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0020_auto_20181112_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garden',
            name='serial',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='outlet',
            name='uvb_end_date',
            field=models.DateField(default=datetime.date(2019, 2, 11)),
        ),
    ]
