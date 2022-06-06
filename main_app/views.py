from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomUserSerializer, BlogSerializer, RegisterSerializer
from .models import CustomUser, Blog
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics


class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get(self,request,*args,**kwargs):
        user = CustomUser.objects.get(id=request.user.id)
        serializer = CustomUserSerializer(CustomUser)
        return Response(serializer.data)

class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

class CustomerUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('first_name')
    serializer_class = CustomUserSerializer
    
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('published')
    serializer_class = BlogSerializer