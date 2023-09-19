from rest_framework import serializers
from .models import Singer,Song



class SingerSerializer(serializers.ModelSerializer):
    # instead song id i want proper song title
    # it is read only
    # many = True, because of many to many relationship
    song = serializers.StringRelatedField(many=True,read_only=True)  
    
    # song = serializers.PrimaryKeyRelatedField(many=True,read_only=True)  
    # song = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')  
    # song = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')  
    # used following in hyperlinked serializer
    # song = serializers.HyperlinkedIdentityField(view_name='song-detail')  
    
    class Meta:
        model = Singer
        fields = ['id','name','gender','song']

class SongSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Song
        fields = ['id','title','singer','duration']

   