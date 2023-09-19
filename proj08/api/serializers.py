from rest_framework import serializers
from .models import Student

# validator
# def starts_with_k(value):
#     if value[0].lower() != 'k':
#         raise serializers.ValidationError('Name should start with K')  

class StudentSerializer(serializers.ModelSerializer):
    def starts_with_k(value):
        if value[0].lower() != 'k':
            raise serializers.ValidationError('Name should start with K')  
    
    name = serializers.CharField(validators=[starts_with_k])
    class Meta:
        model = Student
        fields = ['name','roll','city']

    # field level validation
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value    
    
    #object level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'kush' and ct.lower() != 'indor':
            raise serializers.ValidationError('City must be Indor')
        return data

    

        