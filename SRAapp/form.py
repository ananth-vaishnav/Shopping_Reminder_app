from django.forms import ModelForm # type: ignore
from .models import *
class   Shopform(ModelForm):
    class Meta:
        model = Shop
        fields = ['name','email','location','category','number']
    