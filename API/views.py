from django.shortcuts import render, get_object_or_404
from .models import Member
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserApiView(APIView):
    serializer_class = UserSerializer
    permission_classes = {}  # Add your permissions here

    # GET request - Retrieve a list of users
    def get(self, request):
        users = Member.objects.all()
        serializers = UserSerializer(users, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    # POST request - Create a new user
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT request - Update an existing user
    def put(self, request, pk, *args, **kwargs):
        user = get_object_or_404(Member, pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE request - Delete a user
    def delete(self, request, pk, *args, **kwargs):
        user = get_object_or_404(Member, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
