# Generated by Django 4.2.4 on 2023-09-05 16:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spa_app', '0004_alter_habit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(default=datetime.time(21, 59, 51, 996244), verbose_name='habit starts'),
        ),
    ]