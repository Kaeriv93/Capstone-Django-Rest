from django.contrib import admin
from .models import CustomUser, Blog

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username","first_name","last_name","email","date_of_birth", "avatar", 'bio', 'location' )
admin.site.register(Blog)