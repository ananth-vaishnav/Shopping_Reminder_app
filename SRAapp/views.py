from django.shortcuts import render
from django.views import View

# Create your views here.

class SuperMarket(View):
    def get(self, request):
        return render(request, 'Administrator/supermarket.html')