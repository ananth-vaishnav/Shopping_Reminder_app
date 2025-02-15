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

class Categorytable(models.Model):
    category=models.CharField(max_length=100, blank=True, null=True)

class Product(models.Model):
    shop=models.ForeignKey(Shop,on_delete=models.CASCADE, blank=True,null=True)
    category=models.ForeignKey(Categorytable,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    price=models.IntegerField(null=True,blank=True)
    image=models.FileField(upload_to='product/', blank=True,null=True)

class Feedbacktable(models.Model):
    Feedback = models.CharField(max_length=100, blank=True, null=True)

class Grouptable(models.Model):
    groupname=models.CharField(max_length=100, blank=True, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
class CircleMembers(models.Model):
    member_id=models.ForeignKey(LoginModel,on_delete=models.CASCADE, blank=True,null=True)
    group_id=models.ForeignKey(Grouptable,on_delete=models.CASCADE, blank=True,null=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE, blank=True,null=True)
    role=models.CharField(max_length=100, blank=True,null=True)

class Notification(models.Model):
    Notification_id=models.ForeignKey(LoginModel,on_delete=models.CASCADE, blank=True,null=True)
    circle_id=models.ForeignKey(Grouptable,on_delete=models.CASCADE, blank=True,null=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE, blank=True,null=True)
    message=models.CharField(max_length=100, blank=True,null=True)



class items(models.Model):
    
    group_id=models.ForeignKey(Grouptable,on_delete=models.CASCADE, blank=True,null=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE, blank=True,null=True)
    name = models.CharField(max_length=100, blank=True,null=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE, blank=True,null=True)
    buyer_id=models.ForeignKey(Shop,on_delete=models.CASCADE, blank=True,null=True)
