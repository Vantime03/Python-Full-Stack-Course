# Generated by Django 3.0.1 on 2020-01-14 20:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0018_auto_20200114_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='checkout_date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 15, 2, 32, 34, 287980, tzinfo=utc)),
        ),
    ]
