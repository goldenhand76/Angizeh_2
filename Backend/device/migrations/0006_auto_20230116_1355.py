# Generated by Django 3.2 on 2023-01-16 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0005_auto_20230105_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actuator',
            name='part_number',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='part_number',
            field=models.CharField(max_length=16),
        ),
    ]
