# Generated by Django 3.0.1 on 2020-01-14 02:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0009_auto_20200113_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='checkout_date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 14, 8, 18, 38, 890313, tzinfo=utc)),
        ),
    ]
