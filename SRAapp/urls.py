
from django.urls import include, path # type: ignore

from .views import *

urlpatterns = [
    path('viewshop', viewshop.as_view(),name='viewshop'),
    path('',Login.as_view(),name='login'),
    path('shopregistration',shopregistration.as_view(),name='shopregistration'),
    path('viewuser', viewuser.as_view(),name='viewuser'),
    path('viewfeedback',viewfeedback.as_view(),name='viewfeedback'),
    path('AdminDash',AdminDash.as_view(),name='AdminDash'),
    path('ShopDash',ShopDash.as_view(),name='ShopDash'),
    ###############api
    path('UserReg',UserReg.as_view(),name='UserReg'),
    path('LoginPage',LoginPage.as_view(),name='LoginPage'),
    path('GrouptableAPIView',GrouptableAPIView.as_view(),name='GrouptableAPIView'),

    path('LoginPageApi', LoginPageApi.as_view(),name='LoginPageApi'),
    # path('SendComplaintApi', SendComplaintApi.as_view(),name='SendComplaintApi'),
     path('circlemembers/', CircleMembersAPIView.as_view(), name='circlemembers-list'),
    path('circlemembers/<int:pk>/', CircleMembersAPIView.as_view(), name='circlemembers-detail'),


]
