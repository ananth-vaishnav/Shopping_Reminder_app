from urllib import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
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
        return render(request, 'Administrator/index.html') 
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
    


# //////////////////////////////////////// API /////////////////////////////////////////////
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
class UserReg(APIView):
    def post(self,request):
        print("###############",request.data)
        user_serial=Userserializer(data=request.data)
        login_serial=LoginModelserializer(data=request.data)
        data_valid=user_serial.is_valid()
        login_valid=login_serial.is_valid()

        if data_valid and login_valid:
            print("&&&&&&&&&&&&&&&")
            password=request.data['password']
            login_profile=login_serial.save(type='USER',password=password)
            user_serial.save(LOGINID=login_profile)
            return Response(user_serial.data, status=status.HTTP_201_CREATED)
        return Response({'login_error':login_serial.errors if not login_valid else None,
                        'user_error':user_serial.errors if not data_valid else None},status=status.HTTP_201_CREATED)
    

from rest_framework.views import APIView
from rest_framework.status import *
class LoginPage(APIView):
    def post(self, request):
        response_dict = {}

        # Get data from the request
        username = request.data.get("username")
        password = request.data.get("password")

        # Validate input
        if not username or not password:
            response_dict["message"] = "failed"
            return Response(response_dict, status=HTTP_400_BAD_REQUEST)

        # Fetch the user from LoginTable
        t_user = LoginModel.objects.filter(username=username).first()

        if not t_user:
            response_dict["message"] = "failed"
            return Response(response_dict, status=HTTP_401_UNAUTHORIZED)

        # Successful login response
        response_dict["message"] = "success"
        response_dict["login_id"] = t_user.id

        return Response(response_dict, status=HTTP_200_OK)



from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK


class LoginPageApi(APIView):
    def post(self, request):
        response_dict= {}
        password = request.data.get("password")
        print("Password ------------------> ",password)
        username = request.data.get("username")
        print("Username ------------------> ",username)
        try:
            user = Usermodel.objects.filter(username=username, password=password).first()
            print("user_obj :-----------", user)
        except Usermodel.DoesNotExist:
            response_dict["message"] = "No account found for this username. Please signup."
            return Response(response_dict, HTTP_200_OK)
      
        if user.Type == "student":
            response_dict = {
                "login_id": str(user.id),
                "user_type": user.Type,
                "status": "success",
            }   
            print("User details :--------------> ",response_dict)
            return Response(response_dict, HTTP_200_OK)
        else:
            response_dict["message "] = "Your account has not been approved yet or you are a CLIENT user."
            return Response(response_dict, HTTP_200_OK)
        

# class SendComplaintApi(APIView):
#     def get(self, request, lid):
#         obj = Complaint.objects.filter(STUDENT__LOGIN_id=lid)
#         print("%%%%%%%%%%%%%%",obj)
#         complaint_serializer = ComplaintSerializer(obj, many=True)
#         return Response(complaint_serializer.data)
#     def post(self, request,lid):
#         comp_serializer = SendComplaintSerializer(data=request.data)
#         user_obj = Student.objects.get(LOGIN_id=lid)
#         if comp_serializer.is_valid():
#             comp_serializer.save(STUDENT=user_obj, reply="pending")
#             return Response(comp_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(comp_serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)

class GrouptableAPIView(APIView):
    
    def get(self, request, pk=None):
        if pk:
            group = get_object_or_404(Grouptable, pk=pk)
            serializer = GrouptableSerializer(group)
            return Response(serializer.data)
        groups = Grouptable.objects.all()
        serializer = GrouptableSerializer(groups, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GrouptableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        group = get_object_or_404(Grouptable, pk=pk)
        serializer = GrouptableSerializer(group, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import CircleMembers
from .serializers import CircleMembersSerializer

class CircleMembersAPIView(APIView):
    
    def get(self, request, pk=None):
        if pk:
            member = get_object_or_404(CircleMembers, pk=pk)
            serializer = CircleMembersSerializer(member)
            return Response(serializer.data)
        members = CircleMembers.objects.all()
        serializer = CircleMembersSerializer(members, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CircleMembersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        member = get_object_or_404(CircleMembers, pk=pk)
        serializer = CircleMembersSerializer(member, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
