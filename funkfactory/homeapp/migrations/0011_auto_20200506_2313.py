# Generated by Django 3.0.6 on 2020-05-06 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0010_contactform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 6, 23, 13, 39, 479712)),
        ),
    ]
