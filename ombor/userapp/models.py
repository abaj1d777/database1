from django.contrib.auth.models import User
from django.db import models

class Ombor(models.Model):
    ism = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    manzil = models.CharField(max_length=200)
    dokon =  models.CharField(max_length=200)
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.ism