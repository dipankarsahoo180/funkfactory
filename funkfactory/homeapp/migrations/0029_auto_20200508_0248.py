# Generated by Django 3.0.6 on 2020-05-07 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0028_auto_20200508_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='review',
            field=models.CharField(default='review is mast', max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactform',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 8, 2, 47, 54, 601714)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 8, 2, 47, 54, 601714)),
        ),
    ]
