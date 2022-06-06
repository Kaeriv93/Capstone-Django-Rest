from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomUserSerializer, BlogSerializer
from .models import CustomUser, Blog

class CustomerUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('first_name')
    serializer_class = CustomUserSerializer
    
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('published')
    serializer_class = BlogSerializer