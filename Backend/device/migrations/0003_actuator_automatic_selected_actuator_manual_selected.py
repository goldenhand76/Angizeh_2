# Generated by Django 4.0.1 on 2022-10-03 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0002_alter_actuator_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='actuator',
            name='automatic_selected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='actuator',
            name='manual_selected',
            field=models.BooleanField(default=False),
        ),
    ]
