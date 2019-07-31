from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from filk import models
import json
# Create your views here.

@csrf_exempt
def getdata(request):
    obj=models.JstShowData.objects.latest('id')
    msg={'orderpay':obj.amount_total,'ordernum':obj.order_num,'personnum':obj.person_num}
    # obj1 = models.TempOrder.objects.get(obj.id-1)

    return getresponse(msg)

def getresponse(msg):
    response = HttpResponse(json.dumps(msg), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

@csrf_exempt
def showpage(request):
    return render(request, 'rtime.html')