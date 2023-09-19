from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['city']
    # you can search based on city or name
    # search_fields = ['name','city']
    # search_fields = ['^name']
    # search_fields = ['=city']

  


