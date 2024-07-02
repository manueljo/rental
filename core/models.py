from django.db import models
from django.contrib.auth.models import AbstractUser
from geoposition.fields import GeopositionField

class User(AbstractUser):
    pass

    def __str__(self):
        return str(self.username)
    
class Areas(models.Model):
    name = models.CharField(max_length=50)
    location = GeopositionField()
    
    def __str__(self):
        return self.name

class Apartment(models.Model):
    name = models.CharField(max_length=50)
    area = models.ForeignKey(Areas, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    available = models.BooleanField(default=True)
    location = GeopositionField()
    description = models.TextField()
    room_image = models.ImageField(upload_to='apartments')
    toilet_image = models.ImageField(upload_to='apartments')
    kitchen_image = models.ImageField(blank=True, null=True,upload_to='apartments')
    outside_image = models.ImageField(blank=True, null=True,upload_to='apartments')
    date_uploaded = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name