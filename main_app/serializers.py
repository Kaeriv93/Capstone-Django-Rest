from rest_framework import serializers
from .models import CustomUser, Blog
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    blogs = serializers.SlugRelatedField(
        many = True,
        read_only = True,
        slug_field='content'
    )
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','bio','avatar','location','date_of_birth','name','username','blogs')
qs = CustomUser.objects.prefetch_related('blogs')

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators =[UniqueValidator(queryset = CustomUser.objects.all())]
    )
    password = serializers.CharField(
        write_only = True, required = True, validators =[validate_password])
    password2 = serializers.CharField(write_only = True, required = True)
    class Meta:
        model = CustomUser
        fields = ('username','password','password2','email','first_name','last_name')
        extra_kwargs ={
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    def create(self, validated_data):
        user = CustomUser.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

        
class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields =('content','published')