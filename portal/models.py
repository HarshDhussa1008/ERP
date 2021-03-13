from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tenant(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=50, help_text='Shop Name')
    tenant_name = models.CharField(max_length=50, help_text='Shop owner name')
    rent=models.FloatField(help_text='Monthly rent')
    datetime = models.DateTimeField(help_text='Contract ending date')
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    phone_number = models.CharField(max_length=12)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.shop_name
        
