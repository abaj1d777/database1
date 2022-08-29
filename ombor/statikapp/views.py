from django.shortcuts import render
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.views import APIView
from userapp.models import Ombor
from asosiy.serializers import StatsSerializers
from . models import *

class StetsApiView(APIView):
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [ "client","sana","mahsulot",]
    ordening_fields = ["sana"]
    def get(self,request):
        o = Ombor.objects.get(user=request.user)
        s = Stats.objects.filter(ombor = o)
        ser = StatsSerializers(data = s)
        return Response(ser.data)
    def post(self, request):
        malumot=request.data
        ser = StatsSerializers(data=malumot)
        if ser.is_valid():
            o = Ombor.objects.get(user = request.user)
            ser.save(ombor = o)
        return Response(ser.data)
class StetsApi(APIView):
    def get(self,request,pk):
        o = Ombor.objects.get(user = request.user)
        s = Stats.objects.filter(id = pk,ombor = o)
        ser = StatsSerializers(s)
        return Response(ser.data)
    def put(self, request,pk):
        o = Ombor.objects.get(user=request.user)
        s = Stats.objects.get(id=pk)
        if s.ombor != o:
            malumot=request.data
            ser = StatsSerializers(data=malumot)
            if ser.is_valid():
                ser.save(ombor=o)
            return Response(ser.data)
        return Response()


