from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from userapp.models import Ombor
from .serializer import *

class ClentApiView(APIView):
    def get(self,request):
        o = Ombor.objects.get(user=request.user)
        c=Client.objects.filter(ombor=o)
        ser = ClientSerializers(c, many=True)
        return Response(ser.data)
    def post(self, request):
        malumot = request.data
        ser = Client(data=malumot)
        if ser.is_valid():
            o = Ombor.objects.get(user=request.user)
            ser.save(ombor = o)
        return Response(ser.data)

class ClentApi(APIView):
    def get(self, request, pk):
        o = Ombor.objects.get(user=request.user)
        c=Client.objects.get(id=pk,ombor=o)
        ser=ClientSerializers(c)
        return Response(ser.data)
    def put(self, request,pk):
        o = Ombor.objects.get(user=request.user)
        client = Client.objects.get(id=pk)
        if client.ombor == o:
            malumot = request.data
            ser = MahsulotSerializers(data=malumot)
            if ser.is_valid():
                ser.save(ombor=o)
            return Response(ser.data)
        return Response()

class MahsulotApiView(APIView):
    def get(self,request):
        o = Ombor.objects.get(user=request.user)
        m = Mahsulot.objects.filter(ombor=o)
        ser = MahsulotSerializers(m,many=True)
        return Response(ser.data)
    def post(self, request):
        malumot = request.data
        ser = MahsulotSerializers(data=malumot)
        if ser.is_valid():
            o = Ombor.objects.get(user=request.user)
            ser.save(ombor=o)
        return Response(ser.data)
class MahsulotApi(APIView):
    def put(self, request, pk):
        o = Ombor.objects.get(user=request.user)
        mahsulot = Mahsulot.objects.get(id=pk)
        if mahsulot.ombor == o:
            malumot=request.data
            ser = MahsulotSerializers(data=malumot)
            if ser.is_valid():
                ser.save(ombor=o)
            return Response(ser.data)
        return Response()
