from django.db import models # type: ignore

# Create your models here.

class LoginModel(models.Model):
    username = models.CharField(max_length=100, blank=True,null=True)
    password = models.CharField(max_length=100, blank=True,null=True)
    type = models.CharField(max_length=100, blank=True,null=True)

class User(models.Model):
    LOGINID=models.ForeignKey(LoginModel,on_delete=models.CASCADE, blank=True,null=True)
    name = models.CharField(max_length=100, blank=True,null=True)
    email = models.CharField(max_length=100, blank=True,null=True)
    profile_picture = models.FileField(upload_to='profile/', blank=True,null=True)
    number=models.IntegerField(null=True,blank=True)
    
class Shop(models.Model):
    LOGINID=models.ForeignKey(LoginModel,on_delete=models.CASCADE, blank=True,null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    number=models.IntegerField(null=True,blank=True)
    category=models.CharField(max_length=100, blank=True, null=True)

class Feedback(models.Model):
    Feedback = models.CharField(max_length=100, blank=True, null=True)