from django.db import models

class Job(models.Model):
    images= models.ImageField(upload_to='images/')
    summary =models.CharField(max_length=200)
class User(models.Model):
    usename=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
