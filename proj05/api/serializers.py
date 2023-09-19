from rest_framework import serializers
from .models import Student

def starts_with_k(value):
    if value[0].lower() != 'k':
        raise serializers.ValidationError("Name should start with K")
    

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=70,validators=[starts_with_k])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=70)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        print(instance.name)
        instance.name = validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value
    
    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError("City must be Ranchi")
        return data
    
        