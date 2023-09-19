from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view(['POST'])
# def hello_world(request):
#     print("Data in request: ",request.data)
#     return Response({'msg':"Hello Dear"})

@api_view(['GET','POST'])
def hello_world(request):
    if request.method == "GET":
        return Response({'msg':'This is get request'})
    if request.method == "POST":
        print("Data in request: ",request.data)
        return Response({'msg':"Hello Dear"},{'data':request.data})