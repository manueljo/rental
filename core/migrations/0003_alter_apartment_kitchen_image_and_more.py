# Generated by Django 5.0.6 on 2024-06-27 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_apartment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='kitchen_image',
            field=models.ImageField(blank=True, null=True, upload_to='apartments'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='outside_image',
            field=models.ImageField(blank=True, null=True, upload_to='apartments'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='room_image',
            field=models.ImageField(upload_to='apartments'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='toilet_image',
            field=models.ImageField(upload_to='apartments'),
        ),
    ]
