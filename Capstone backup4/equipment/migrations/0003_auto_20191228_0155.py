# Generated by Django 3.0.1 on 2019-12-28 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0002_equipment_tool_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='image1',
            field=models.ImageField(default='default1.jpg', upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='image2',
            field=models.ImageField(default='default1.jpg', upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='image3',
            field=models.ImageField(default='default1.jpg', upload_to='profile_pics'),
        ),
    ]