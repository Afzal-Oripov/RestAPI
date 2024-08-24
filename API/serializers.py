from rest_framework import serializers
from .models import Member

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'firstname', 'lastname', 'age']
        