from django.contrib import admin

# Register your models here.

from app_usuario.models import User_profile

@admin.register(User_profile)
class User_profile_admin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'user', 'phone', 'adress', 'image']
