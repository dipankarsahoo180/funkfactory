# Generated by Django 3.0.6 on 2020-05-06 18:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0011_auto_20200506_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('sub_heading', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='contactform',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 7, 0, 16, 34, 295183)),
        ),
    ]
