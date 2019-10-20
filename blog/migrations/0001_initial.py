# Generated by Django 2.0.2 on 2018-11-13 00:18

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('garden', '0021_auto_20181113_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('picture', models.ImageField(upload_to=blog.models.upload_to)),
                ('garden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden.Garden')),
            ],
        ),
    ]
