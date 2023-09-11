# Generated by Django 3.2.20 on 2023-09-11 09:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('time', models.CharField(choices=[('09:00', '09:00'), ('11:30', '11:30'), ('14:00', '14:00'), ('16:30', '16:30')], max_length=20)),
                ('date_of_wedding', models.DateField(default=datetime.date.today)),
                ('no_in_party', models.PositiveSmallIntegerField(help_text='Please note max number of guests is 5 (not including yourself)')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]