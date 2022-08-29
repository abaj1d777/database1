from django.db import models
from userapp.models import Ombor

class Mahsulot(models.Model):
    nom =models.CharField(max_length=200)
    brend = models.CharField(max_length=200)
    kegan_narx = models.SmallIntegerField()
    sotuv_narx = models.SmallIntegerField()
    miqdor = models.SmallIntegerField()
    ombor = models.ForeignKey(Ombor,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Client(models.Model):
    ism = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    manzil = models.CharField(max_length=200)
    dokon = models.CharField(max_length=200)
    qarz = models.IntegerField(default=0)
    ombor = models.ForeignKey(Ombor,on_delete= models.CASCADE)
    def __str__(self):
        return self.ism



