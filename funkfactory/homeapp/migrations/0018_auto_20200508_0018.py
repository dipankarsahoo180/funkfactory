# Generated by Django 3.0.6 on 2020-05-07 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0017_auto_20200508_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='more_popup_image',
            field=models.ImageField(null=True, upload_to='cards'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 8, 0, 18, 34, 225152)),
        ),
    ]
