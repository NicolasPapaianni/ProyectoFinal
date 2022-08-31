from django.db import models


class User_profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name= 'perfil')
    phone = models.CharField(max_length=15, blank=True)
    adress = models.CharField(max_length= 150, blank=True)
    image = models.ImageField(upload_to = 'perfil_image/', blank=True)


