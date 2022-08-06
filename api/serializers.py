from dataclasses import fields
from pyexpat import model
from turtle import pos
from rest_framework import serializers
from .models import CustomUser,Post

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'
        extra_kwargs={
            'password':{'write_only':True}
        }


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'        