# Generated by Django 5.0.6 on 2024-06-25 16:47

import django.db.models.deletion
import geoposition.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField(null=True)),
                ('available', models.BooleanField(default=True)),
                ('location', geoposition.fields.GeopositionField(max_length=42)),
                ('description', models.TextField()),
                ('room_image', models.ImageField(upload_to='')),
                ('toilet_image', models.ImageField(upload_to='')),
                ('kitchen_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('outside_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.areas')),
            ],
        ),
    ]
