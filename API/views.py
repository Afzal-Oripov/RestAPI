from django.shortcuts import render
from .models import Member
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserApiView(APIView):
    serializer_class = UserSerializer
    permission_classes = {}
    # get zapros
    def get(self, request):
        users = Member.objects.all()
        serializers = UserSerializer(users, many=True, context= {'request':request})
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    # post zapros
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        