# Generated by Django 3.0.6 on 2020-05-09 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0034_auto_20200508_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwords',
            name='first_name',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='passwords',
            name='last_name',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 9, 12, 23, 26, 849436)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 9, 12, 23, 26, 849436)),
        ),
    ]
