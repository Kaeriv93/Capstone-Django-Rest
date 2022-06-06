from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length= 100)
    avatar = models.CharField(max_length = 2000, default='https://as1.ftcdn.net/v2/jpg/03/53/11/00/1000_F_353110097_nbpmfn9iHlxef4EDIhXB1tdTD0lcWhG9.jpg')
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length = 1000)
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['name']

