# Generated by Django 3.0.6 on 2020-05-10 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0039_auto_20200510_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=15)),
                ('image1', models.ImageField(blank=True, upload_to='background')),
                ('image2', models.ImageField(blank=True, upload_to='background')),
                ('image3', models.ImageField(blank=True, upload_to='background')),
            ],
            options={
                'verbose_name': 'Details',
                'verbose_name_plural': '912 Background Image',
            },
        ),
        migrations.AlterField(
            model_name='contactform',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 23, 23, 15, 871686)),
        ),
        migrations.AlterField(
            model_name='homepictures',
            name='title',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 23, 23, 15, 861695)),
        ),
    ]
