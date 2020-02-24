from django.db import models
from django.conf.urls import url, include
#from django.contrib.auth.models import User
from rest_framework import serializers

from wakerfarmer.models import *

class MillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mill
        fields = [ 'mid', 'name', 'lat', 'lng' ]

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = [ 'fid', 'first_name', 'last_name', 'username', 'call' ]

class OwnermillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ownermill
        fields = [ 'qid', 'first_name', 'last_name', 'username' ]

class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queue
        fields = [ 'qid', 'mill', 'farmer', 'queue' ]

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = [ 'pid', 'mill', 'farmer', 'price', 'sprice' ]
