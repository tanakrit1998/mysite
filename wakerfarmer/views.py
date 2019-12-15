import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

from .models import *

# Create your views here.
def index(req):
    return render(req, 'wakeupfarmer/index.html')

def apimills(req):
    mills = Mill.objects.all()
    data = serializers.serialize('json', mills)
    return HttpResponse(data, content_type='application/json')

def api_get_close_mills(req, lat, lng, distance='5.0'):
    distance = float(distance)
    mills = Mill.objects.all()
    result = []
    for mill in mills:
        if mill.lat == lat-0.0001 and mill.lng == lng-0.0001:
            result.append( mill )
    data = serializers.serialize('json', result)
    return HttpResponse(data, mimetype='application/json')
