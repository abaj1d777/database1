
from rest_framework import generics
from asosiy.serializers import OmborSerializers,OmborSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from userapp.models import *




class OmborApi(APIView):
    def get(self, request,pk):
        o = Ombor.objects.get(user=self.request.user)
        ser=OmborSerializers(o)
        return Response(ser.data)

class UserView(generics.RetrieveUpdateDestroyAPIView):
        queryset = User.objects.all()
        serializer_class = OmborSerializers

class Userlar(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class = OmborSerializers


