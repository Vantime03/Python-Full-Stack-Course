# Generated by Django 3.0.1 on 2020-01-23 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0030_auto_20200114_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
