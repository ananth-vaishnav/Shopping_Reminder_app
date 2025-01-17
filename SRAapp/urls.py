
from django.urls import include, path

from .views import *

urlpatterns = [
    path('viewshop', viewshop.as_view(),name='viewshop'),
    path('',Login.as_view(),name='login'),
    path('shopregistration',shopregistration.as_view(),name='shopregistration'),
    path('viewuser', viewuser.as_view(),name='viewuser'),
    path('viewfeedback',viewfeedback.as_view(),name='viewfeedback'),
    path('AdminDash',AdminDash.as_view(),name='AdminDash'),
    path('ShopDash',ShopDash.as_view(),name='ShopDash'),
]
