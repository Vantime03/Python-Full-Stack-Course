# Generated by Django 3.0.1 on 2020-01-06 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0003_auto_20191228_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='image1',
            field=models.ImageField(default='default1.png', upload_to='equipment_pics'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='image2',
            field=models.ImageField(default='default1.png', upload_to='equipment_pics'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='image3',
            field=models.ImageField(default='default1.png', upload_to='equipment_pics'),
        ),
    ]