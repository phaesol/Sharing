from django.shortcuts import render,get_object_or_404
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .serializers import PostSerializer,CategorySerializer
from .models import Category, Post
from rest_framework import viewsets,permissions
from rest_framework.response import Response


# class UserViewSet(viewsets.ModelViewSet):
    
#     queryset = CustomUser.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-created_at')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
 



       