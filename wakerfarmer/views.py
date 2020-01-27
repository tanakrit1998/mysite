import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *

# Create your views here.
def index(req):
    return render(req, 'wakeupfarmer/index.html')

def apimills(req):
    if req.method == 'GET':
        print( req.GET )
        mills = Mill.objects.all()
        data = serializers.serialize('json', mills)
        return HttpResponse(data, content_type='application/json')

def apimills_by_price(req):
    if req.method == 'GET':
        print( req.GET )
        mills = Mill.objects.order_by('-price','-sprice')
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

@csrf_exempt
def api_login(req):
    data = { 
        'message': 'login fails' 
    }
    if req.method == 'POST':
        a = str(req.body)
        a = a[3:-2].split(',')
        username = a[0].split(':')[1]
        password = a[1].split(':')[1]
        username = username.strip().replace('"', '')
        password = password.strip().replace('"', '')
        print(f'เขาส่ง username= "{username}"')
        print(f'เขาส่ง password= "{password}"')
        farmers = Farmer.objects.filter(username=username, password=password)
        if farmers: # ถ้าค้นเจอ
            data = { 
                'user': 'Boss',
                'message': 'login success' 
            }
    return HttpResponse(json.dumps(data), content_type = 'application/javascript; charset=utf8')
