from rest_framework import serializers
from .models import CustomUser, Blog

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
        
class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields =('content','published')