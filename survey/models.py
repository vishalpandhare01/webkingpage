from email import message
from django.db import models
from django.forms import CharField

# Create your models here.
class Survey(models.Model):
    full_name=models.CharField(max_length=200)
    age=models.IntegerField()
    web_desing=models.CharField(max_length=200)
    responsive_web=models.CharField(max_length=200)
    web_speed=models.CharField(max_length=200)
    service=models.CharField(max_length=200)
    message=models.TextField()
    feedback=models.TextField()
    rating=models.IntegerField()



