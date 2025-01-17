# Generated by Django 3.0.6 on 2020-05-11 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0042_auto_20200511_2105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactform',
            options={'ordering': ('-date',), 'verbose_name': 'Details', 'verbose_name_plural': '911 Contact forms'},
        ),
        migrations.AlterField(
            model_name='contactform',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 11, 21, 12, 0, 954105)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 11, 21, 12, 0, 949367)),
        ),
    ]
