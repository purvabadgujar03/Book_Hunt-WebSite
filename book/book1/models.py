from django.db import models

# Create your models here.
from django.db.models import Model


class Footer(models.Model):
    name=models.CharField(max_length=15)
    image=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name


class book2(models.Model):
    name=models.CharField(max_length=150)
    im1=models.ImageField(upload_to='images/')
    disc=models.CharField(max_length=500)
    price=models.IntegerField(default=0)
    cart1=models.IntegerField(default=0)
    def __str__(self):
        return self.name

class recommendation(models.Model):
    name=models.CharField(max_length=150)
    im1 = models.ImageField(upload_to='images/')
    disc = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class cutomers(models.Model):
    username=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
    emailid=models.CharField(max_length=30)
    login=models.CharField(max_length=15)
    def __str__(self):
        return  self.username














