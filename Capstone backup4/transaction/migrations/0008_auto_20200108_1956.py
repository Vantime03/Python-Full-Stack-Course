# Generated by Django 3.0.1 on 2020-01-09 03:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0007_auto_20200108_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='checkout_date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 9, 9, 56, 51, 517678, tzinfo=utc)),
        ),
    ]
