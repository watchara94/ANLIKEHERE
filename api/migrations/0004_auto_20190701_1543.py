# Generated by Django 2.1.1 on 2019-07-01 08:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190622_0046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refridgerator_display_system',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='refridgerator_display_system',
            name='status',
        ),
        migrations.AddField(
            model_name='refridgerator_display_system',
            name='datetime_regis',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 1, 8, 43, 13, 531404, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='history',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 1, 8, 43, 13, 531404, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='refridgerator_display_system',
            name='name',
            field=models.TextField(default=''),
        ),
    ]
