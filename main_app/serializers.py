from rest_framework import serializers
from .models import  Blog, CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name','last_name','bio','avatar','location','date_of_birth', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            bio =validated_data['bio'],
            avatar=validated_data['avatar'],
            location=validated_data['location'],
            date_of_birth=validated_data['date_of_birth']
            
            )

        user.set_password(validated_data['password'])
        user.save()

        return user

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    blogs = serializers.SlugRelatedField(
        many = True,
        read_only = True,
        slug_field='content'
    )
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','bio','avatar','location','date_of_birth','username','blogs','password')
qs = CustomUser.objects.prefetch_related('blogs')

        
class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields =('content','published')