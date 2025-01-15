
from django.urls import include, path

from .views import *

urlpatterns = [
    path('supermarket', SuperMarket.as_view(),name='supermarket'),
]
