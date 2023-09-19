from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=70)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=70)
