from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

from .models import Post
from .permissions import IsAuthenticatedAndOwner
from .serializers import PostSerializer, UserSerializer
# Create your views here.

# class PostList(ListCreateAPIView):
#     # authentication_classes = [TokenAuthentication]
#     permission_classes = (IsAuthenticatedAndOwner, )
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticatedAndOwner, )
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedAndOwner, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser, )
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
