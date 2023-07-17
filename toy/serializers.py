from rest_framework import serializers
from toy.models import Toy

class ToySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    description = serializers.CharField(default="")
    release_date = serializers.DateTimeField()
    category = serializers.CharField(max_length=50)
    was_included_in_home = serializers.BooleanField(default=False)
    
    def create(self, validated_data):
        return Toy.objects.create(**validated_data)
        
        
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.was_included_in_home = validated_data.get('was_included_in_home', instance.was_included_in_home)
        instance.save()
        return instance