from rest_framework import serializers
from .models import *


class   LoginModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=LoginModel
        fields=['username','password','type']

class   Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['LOGINID','name','email','profile_picture','number']

class   Shopserializer(serializers.ModelSerializer):
    class Meta:
        model=Shop
        fields=['LOGINID','name','email','location','number','category']
        
class   Feedbackserializer(serializers.ModelSerializer):
    class Meta:
        model=Feedbacktable
        fields=['Feedback']


class CircleMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CircleMembers
        fields = ['member_id','circle_id','user_id','message']

class GrouptableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grouptable
        fields = ['groupname','user']
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['message','circle_id','user_id','Notification_id']


class itemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = items
        fields = ['item_id','circle_id','user_id','category_id','buyer_id','name']
        


