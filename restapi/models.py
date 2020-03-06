from django.db import models
from django.conf.urls import url, include
#from django.contrib.auth.models import User
from rest_framework import serializers

from wakerfarmer.models import *

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = [ 'fid', 'first_name', 'last_name', 'username', 'call' ]

class OwnermillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ownermill
        fields = [ 'oid', 'first_name', 'last_name', 'username' ]

class MillSerializer(serializers.ModelSerializer):
    ownermill = OwnermillSerializer(read_only=True)
    class Meta:
        model = Mill
        fields = [ 'mid', 'name', 'lat', 'lng', 'ownermill' ]

class QueueSerializer(serializers.ModelSerializer):
    mill = MillSerializer(read_only=True)
    farmer = FarmerSerializer(read_only=True)
    class Meta:
        model = Queue
        fields = [ 'qid', 'mill', 'farmer', 'queue' ]

class PriceSerializer(serializers.ModelSerializer):
    mill = MillSerializer(read_only=True)
    farmer = FarmerSerializer(read_only=True)
    class Meta:
        model = Price
        fields = [ 'pid', 'mill', 'farmer', 'price', 'sprice' ]
