# Generated by Django 3.0.6 on 2020-05-07 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0018_auto_20200508_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
