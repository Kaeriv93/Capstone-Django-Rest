from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','bio','avatar','location','date_of_birth','name','username')