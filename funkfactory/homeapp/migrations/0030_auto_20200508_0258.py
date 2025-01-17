# Generated by Django 3.0.6 on 2020-05-07 21:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0029_auto_20200508_0248'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('add_line_1', models.CharField(blank=True, max_length=30)),
                ('add_line_2', models.CharField(blank=True, max_length=30)),
                ('add_line_3', models.CharField(blank=True, max_length=30)),
                ('phone_line_1', models.CharField(blank=True, max_length=20)),
                ('phone_line_2', models.CharField(blank=True, max_length=20)),
                ('phone_line_3', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='contactform',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 8, 2, 58, 27, 493843)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 8, 2, 58, 27, 497840)),
        ),
    ]
