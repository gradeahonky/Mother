# Generated by Django 2.0.2 on 2018-09-24 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0002_garden_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='garden',
            name='user',
        ),
    ]
