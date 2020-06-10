from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ClientInfo(models.Model):
    #THIS IS LIKE EXTENDING THE CLASS TO ADD MORE FIELDS
    client = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    #Adding the additional fields
    date = models.DateField()
    phone_number = models.CharField(max_length=13) #note, it does'nt start with models

    def __str__(self):
        return self.client.username
        #username is a default attribute
class Booking(models.Model):
    username = models.CharField(max_length=30,unique=False)
    email = models.EmailField(max_length=30,unique=True,blank=True)
    date = models.DateField()
    phone_number = models.CharField(max_length=13) #note, it does'nt start with models

    def __str__(self):
        return self.username
