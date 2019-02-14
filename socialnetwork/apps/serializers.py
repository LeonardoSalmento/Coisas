from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.db import transaction

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('url','id','username','email','address')


class PostSerializer(serializers.ModelSerializer):
    userId = ProfileSerializer(serializers.ModelSerializer)


    class Meta:
        model = Post
        fields = ('id','title','body','userId')


class CommentSerializer(serializers.ModelSerializer):
    postId = PostSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id','name','body','email', 'postId')
