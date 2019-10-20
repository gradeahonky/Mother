# Generated by Django 2.0.2 on 2018-10-30 21:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0017_auto_20181030_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='outlet',
            name='uvb_end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='outlet',
            name='uvb_start_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='garden',
            name='stage',
            field=models.CharField(choices=[('SEEDLING', 'Seedling'), ('VEGETATIVE', 'Vegetative'), ('FLOWER', 'Flower')], default='Seedling', max_length=10),
        ),
    ]
