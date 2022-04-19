import email
from email import message
from django.db import models

# Create your models here.
class webking(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=300)
    phone=models.IntegerField()
    email=models.EmailField()
    
    