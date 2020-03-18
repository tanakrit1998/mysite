import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max

from .models import *

# Create your views here.
def index(req):
    return render(req, 'wakeupfarmer/index.html')

@csrf_exempt
def apimills(req):
    if req.method == 'GET':
        print( req.GET )
        mills = Mill.objects.all()
        data = serializers.serialize('json', mills)
        return HttpResponse(data, content_type='application/json')

@csrf_exempt
def api_max_queue(req, mid=0): # queue ห้ามลด ต้องเพิ่มตลอด
    if req.method == 'GET':
        queue.queue = Queue.objects.aggregate(Max('queue'))
        queue.save()

        data = serializers.serialize('json', list(queue))
        return HttpResponse(data, content_type='application/json')

@csrf_exempt
def api_add_queue(req, mid=0, fid=0): # queue ห้ามลด ต้องเพิ่มตลอด
    #if req.method == 'GET':
    queue = Queue()
    mill = Mill.objects.get(pk=mid)
    queue.mill = mill
    farmer = Farmer.objects.get(pk=fid)
    queue.farmer = farmer
    queue.queue = Queue.objects.filter(mill=queue.mill).aggregate(Max('queue'))['queue__max']+1
    queue.save()

    data = serializers.serialize('json', [ queue, mill, farmer ])
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def api_delete_queue(req, qid=0): 
    if req.method == 'POST':
        mills = Mill.objects.all()
        data = serializers.serialize('json', mills)
        return HttpResponse(data, content_type='application/json')

@csrf_exempt
def get_mill(req, mid=0):
    #print(f'mid = {mid}')
    try:
        mill = Mill.objects.get(pk=mid)
        #print(mill)
        data = serializers.serialize('json', [ mill ])
        #print(data)
        return HttpResponse(data, content_type='application/json')
    except:
        print('exception')
    return HttpResponse({}, content_type='application/json')

@csrf_exempt
def update_mill(req, mid=0):
    print(f'mid = {mid}')
    d = json.loads(req.body)
    #print(d)
    if req.method == 'POST':
        #print(mill)
        #print(req.POST)
        mill = Mill.objects.get(pk=mid)
        mill.queue = int(d['queue'])
        mill.save()
        data = serializers.serialize('json', [mill])
        return HttpResponse(data, content_type='application/json')

    return HttpResponse({}, content_type='application/json')

def apimills_by_price(req):
    if req.method == 'GET':
        print( req.GET )
        #mills = Mill.objects.order_by('-price','-sprice')
        prices = Price.objects.order_by('-price').values()
        #print(prices)
        #data = serializers.serialize('json', prices)
        #return HttpResponse(data, content_type='application/json')    
        return JsonResponse(list(prices), safe=False)    

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
                'message': 'login success' ,
            }
    return HttpResponse(json.dumps(data), content_type = 'application/javascript; charset=utf8')

@csrf_exempt
def api_login_owner(req):
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
        ownermills = Ownermill.objects.filter(username=username, password=password)
        if ownermills: # ถ้าค้นเจอ
            data = { 
                'user': 'Boss',
                'message': 'loginowner success' ,
            }
    return HttpResponse(json.dumps(data), content_type = 'application/javascript; charset=utf8')    

@csrf_exempt
def api_register_farmer (req) : 
    data = { 
        'user': '',
        'name': '',
        'password': '',
        'message': 'login fails', 
    }
    if req.method == 'POST':
        a = str(req.body)
        a = a[3:-2].split(',')
        first_name = a[0].split(':')[1]
        last_name = a[1].split(':')[1]
        username = a[2].split(':')[1]
        password = a[3].split(':')[1]
        call     = a[4].split(':')[1]

        first_name = first_name.strip().replace('"','')
        last_name = last_name.strip().replace('"','')
        username = username.strip().replace('"', '')
        password = password.strip().replace('"', '')
        call    = call.strip().replace('"','')

        print(f'เขาส่ง username= "{username}"')
        print(f'เขาส่ง password= "{password}"')
        if first_name != '' and last_name != '' and username != '' and password != '' and call != '':
            try:
                farmers = Farmer()
        
                farmers.first_name = first_name
                farmers.last_name =last_name
                farmers.username = username
                farmers.password = password
                farmers.call    = call
                farmers.save()
                print(f'เขาส่ง password= "{password}"')
                if farmers: # ถ้าค้นเจอ
                    data = {
                        'first_name': farmers.first_name,
                        'last_name': farmers.last_name,
                        'user': farmers.username,
                        'password': farmers.password,
                        'call': farmers.call,
                        'message': 'register success' ,
                    }
            except: pass
    return HttpResponse(json.dumps(data), content_type = 'application/javascript; charset=utf8')

@csrf_exempt
def api_register_ownermill (req) : 

    data = { 
        'user': '',
        'name': '',
        'password': '',
        'message': 'register fails', 
    }
    if req.method == 'POST':
        a = str(req.body)
        a = a[3:-2].split(',')
        first_name = a[0].split(':')[1]
        last_name = a[1].split(':')[1]
        username = a[2].split(':')[1]
        password = a[3].split(':')[1]
        

        first_name = first_name.strip().replace('"','')
        last_name = last_name.strip().replace('"','')
        username = username.strip().replace('"', '')
        password = password.strip().replace('"', '')
        

        print(f'เขาส่ง username= "{username}"')
        print(f'เขาส่ง password= "{password}"')
        if first_name != '' and last_name != '' and username != '' and password != '':

            try:
                ownermill = Ownermill()
        
                ownermill.first_name = first_name
                ownermill.last_name =last_name
                ownermill.username = username
                ownermill.password = password
                
                ownermill.save()
                
                if ownermill: # ถ้าค้นเจอ
                    data = {
                        'first_name': ownermill.first_name,
                        'last_name': ownermill.last_name,
                        'user': ownermill.username,
                        'password': ownermill.password,
                        'message': 'register success' ,
                    }
            except: pass
    return HttpResponse(json.dumps(data), content_type = 'application/javascript; charset=utf8')

