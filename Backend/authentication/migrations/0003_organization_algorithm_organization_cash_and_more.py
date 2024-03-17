# Generated by Django 4.0.1 on 2022-12-16 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_last_name_alter_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='algorithm',
            field=models.CharField(choices=[('FORWARD', 'FORWARD'), ('BACKWARD', 'BACKWARD')], max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='cash',
            field=models.IntegerField(default=100000),
        ),
        migrations.AddField(
            model_name='organization',
            name='sms_price',
            field=models.IntegerField(default=510),
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=6)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
