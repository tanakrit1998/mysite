from django.shortcuts import render

from rest_framework import viewsets

from wakerfarmer.models import *
from .models import *

class MillViewSet(viewsets.ModelViewSet):
    queryset = Mill.objects.all()
    serializer_class = MillSerializer

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class OwnermillViewSet(viewsets.ModelViewSet):
    queryset = Ownermill.objects.all()
    serializer_class = OwnermillSerializer

class QueueViewSet(viewsets.ModelViewSet):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
