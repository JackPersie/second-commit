from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Login(models.Model):
    name = models.CharField(max_length=256, unique=True)
    mail = models.EmailField(unique=True)
    pwd = models.CharField(unique=True, max_length=12)


class Result(models.Model):
    name = models.ForeignKey(Login, on_delete=CASCADE)
