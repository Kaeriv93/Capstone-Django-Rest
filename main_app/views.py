from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomUserSerializer
from .models import CustomUser

class CustomerUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('first_name')
    serializer_class = CustomUserSerializer