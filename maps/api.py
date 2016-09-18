from maps.models import Adventures
from maps.serealizers import AdventureSerializer
from django.http import JsonResponse

###REST 
#from django.shortcuts import render
#from django.http import HttpResponse
#from django.http import HttpRequest
#from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from rest_framework.response import Response
        

@api_view(['GET','POST'])
@csrf_exempt
def adventures(request,userId=None):
    if request.method == 'GET':
        adventures = Adventures.objects.filter(owner_id=userId)
        serializer = AdventureSerializer(adventures,many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        print("IN POST")
        #this needs testing
        data = JSONParser().parse(request)
        print(data)
        serializer = AdventureSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False)#
            #return JSONResponse(serializer.data, status=201)
        else:
            print("serializer doesn't approve")
            return JsonResponse(serializer.errors,status=400)    
        #return JSONResponse(serializer.errors, status=400)