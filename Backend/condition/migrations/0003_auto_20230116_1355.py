# Generated by Django 3.2 on 2023-01-16 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condition', '0002_auto_20230105_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='binary',
            name='checked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='continues',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
