# Generated by Django 3.0.6 on 2020-05-07 19:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0020_auto_20200508_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='contactform',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 8, 0, 31, 13, 88266)),
        ),
    ]
