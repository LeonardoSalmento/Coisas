from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from apps.serializers import *



# Create your views here.

class ProfileView(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	serializer_detail_class = ProfileSerializer


class PostView(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	serializer_detail_class = PostSerializer


class CommentView(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	serializer_detail_class = CommentSerializer