# Generated by Django 3.0.6 on 2020-05-05 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0007_auto_20200506_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='card_title',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cards',
            name='images',
            field=models.ImageField(null=True, upload_to='cards'),
        ),
    ]
