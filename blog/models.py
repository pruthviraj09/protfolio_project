from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images1/')
