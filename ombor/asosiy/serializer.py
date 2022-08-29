from django.contrib.auth.models import User
from .models import  *
from app1.models import Stats
from userapp.models import Ombor
from rest_framework import serializers

s = serializers.ModelSerializer

class OmborSerializers(s):
    class Meta:
        model = Ombor
        fields = "__all__"

class MahsulotSerializers(s):
    class Meta:
        model = Mahsulot
        fields = "__all__"

class ClientSerializers(s):
    class Meta:
        model = Client
        fields = "__all__"

class UserSerializers(s):
    class Meta:
        model = User
        fields = "__all__"

class StatsSerializers(s):
    class Meta:
        model =  Stats
        fields = "__all__"