# Generated by Django 4.0.1 on 2022-10-03 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0003_actuator_automatic_selected_actuator_manual_selected'),
        ('automation', '0002_alter_manualtile_actuator_alter_manualtile_title'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='manualtile',
            name='unique_manual_name',
        ),
        migrations.AlterField(
            model_name='manualtile',
            name='actuator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.actuator'),
        ),
    ]
