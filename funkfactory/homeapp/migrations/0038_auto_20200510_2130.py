# Generated by Django 3.0.6 on 2020-05-10 16:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0037_auto_20200510_2120'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cards',
        ),
        migrations.AlterField(
            model_name='contactform',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 21, 30, 27, 652445)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 21, 30, 27, 652445)),
        ),
    ]