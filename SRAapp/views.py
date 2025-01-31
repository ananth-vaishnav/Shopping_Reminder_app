from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .form import *

from .models import *

# Create your views here.

class viewshop(View):
    def get(self, request):
         d = Shop.objects.all()
         print(d)
         return render(request, 'Administrator/viewshop.html',{'val':d})
    
class Login(View):
    def get(self, request):
        return render(request, 'Administrator/login.html') 
    def post(self,request):
        username= request.POST['username']   
        password= request.POST['password']  
        login_obj=LoginModel.objects.get(username=username,password=password) 
        if login_obj.type=="admin":
            return HttpResponse('''<script>alert("Welcome to Admin page");window.location="AdminDash"</script>''')
        elif login_obj.type=="shop":
            return HttpResponse('''<script>alert("Welcome to Shop page");window.location="/ShopDash"</script>''')
    
    
class shopregistration(View):
    def get(self, request):
        return render(request, 'Administrator/shopregistration.html')  
    def post(self, request):
        form=Shopform(request.POST)
        if form.is_valid():
            var=form.save(commit=False)
            b=LoginModel.objects.create(username=request.POST['email'],password= request.POST['password'],type='shop')
            var.LOGINID=b
            var.save()
            return HttpResponse('''<script>alert("Shop Registered Successfully");window.location="/"</script>''')
    
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