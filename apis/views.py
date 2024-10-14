from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *
# Create your views here.
class TemperatureLogView(generics.ListCreateAPIView):
    queryset = TemperatureLog.objects.all()
    serializer_class = TemperatureLogSerializer