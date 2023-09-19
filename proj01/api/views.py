from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.
'''
def student_detail(request,pk):
    stu = Student.objects.get(id=pk)
    print("stu: ",stu)
    serializer = StudentSerializer(stu)
    print("Serializer: ",serializer)
    print("Data: ",serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    print("Json data: ",json_data)
    return HttpResponse(json_data,content_type='application/json')'''


def student_detail(request,pk):
    stu = Student.objects.get(id=pk)
    print("stu: ",stu)
    serializer = StudentSerializer(stu)
    print("Serializer: ",serializer)
    print("Data: ",serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print("Json data: ",json_data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=True)

def all_students(request):
    stu = Student.objects.all()
    print("stu: ",stu)
    serializer = StudentSerializer(stu,many=True)
    print("Serializer: ",serializer)
    print("Data: ",serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    print("Json data: ",json_data)
    return HttpResponse(json_data,content_type='application/json')
    # return JsonReponse(serializer.data,safe=False) # as non dict data
