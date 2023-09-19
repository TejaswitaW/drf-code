from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        print("json_data: ",json_data)
        stream = io.BytesIO(json_data)
        print("Stream: ",stream)
        pythondata = JSONParser().parse(stream)
        print('PythonData: ',pythondata)
        serializer = StudentSerializer(data=pythondata)
        print('Serializer: ',serializer)
        print(serializer.is_valid())
        #print(serializer.errors)
        if serializer.is_valid():
            print("Inside if after validation")
            serializer.save()
            res = {'msg':"Data Created"}
            json_res = JSONRenderer().render(res)
            return HttpResponse(json_res,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')