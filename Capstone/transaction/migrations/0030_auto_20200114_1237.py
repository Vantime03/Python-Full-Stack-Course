# Generated by Django 3.0.1 on 2020-01-14 20:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0029_auto_20200114_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='checkout_date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]