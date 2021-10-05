from django.db import models

# Create your models here.
class work(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to="pics")
    des=models.TextField()