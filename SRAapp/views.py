from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import *

# Create your views here.

class viewshop(View):
    def get(self, request):
        return render(request, 'Administrator/viewshop.html')
    
class Login(View):
    def get(self, request):
        return render(request, 'Administrator/login.html') 
    def post(self,request):
        username= request.POST['username']   
        password= request.POST['password']  
        login_obj=LoginModel.objects.get(username=username,password=password) 
        if login_obj.type=="admin":
            return HttpResponse('''<script>alert("Welcome to Admin page");window.location="AdminDash"</script>''')
    
    
class shopregistration(View):
    def get(self, request):
        return render(request, 'Administrator/shopregistration.html')   
    
class viewuser(View):
    def get(self, request):
        c = User.objects.all()
        return render(request, 'Administrator/viewuser.html',{'val':c})

class viewfeedback(View):
    def get(self, request):
        return render(request,'Administrator/viewfeedback.html')
    
class AdminDash(View):
    def get(self, request):
        return render(request, 'Administrator/AdminDash.html')  
    
class ShopDash(View):
    def get(self,request):
        return render(request,'Administrator/ShopDash.html')