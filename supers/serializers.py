from rest_framework import serializers
from .models import Super, Superpower

class SuperpowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Superpower
        fields = ['name']

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'name', 'alter_ego', 'superpowers', 'catchphrase', 'super_type']
        depth = 1
        super_type = serializers.IntegerField(write_only=True)
