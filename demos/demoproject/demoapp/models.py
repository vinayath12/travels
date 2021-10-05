from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="pics")
    des = models.TextField()

class People(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="pic")
    des = models.TextField()
