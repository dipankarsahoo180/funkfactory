# Generated by Django 3.0.6 on 2020-05-10 23:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0040_auto_20200510_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 11, 4, 43, 28, 530396)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 11, 4, 43, 28, 525625)),
        ),
    ]