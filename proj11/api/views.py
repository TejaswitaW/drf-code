from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request,pk=None):  
    if request.method == 'GET':
        id = pk
        # id = request.data.get('id')
        '''Above, earlier we were getting first id from request ,
        then we were getting student object using that id,
        earlier our function signature was def student_api(request),
        now pk=None added'''
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        stu = request.data
        serializer = StudentSerializer(data=stu)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors)
    
    if request.method == 'PATCH':
        id = pk
        # id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        id = pk
        # id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu)
        print(serializer.data)
        print(stu)
        stu.delete()
        return Response(serializer.data)
        
