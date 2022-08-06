from django.shortcuts import render
from .serializers import CustomUserSerializer, PostSerializer
from .models import CustomUser, Post
from rest_framework.response import Response
from rest_framework.decorators import api_view
import random

def tokenGenerator():
    materials="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tkn=""
    for i in range(0,10):
        tkn=tkn+random.choice(materials)
    return tkn  

@api_view(['POST'])
def registerView(request):
    if request.data['password']==request.data['password2']:
        token=tokenGenerator()
        request.data['token']=token
        serializer=CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("not valid")    
    else:
        return Response("passwords are not matching") 

@api_view(['POST'])
def loginView(request):
    username=request.data['username'] 
    password=request.data['password']
    user=CustomUser.objects.get(username=username)
    if password==user.password:
        serializer=CustomUserSerializer(user)
        return Response(serializer.data)   
    else:
        return Response()               

@api_view(['GET'])
def showData(request):
    users=CustomUser.objects.all()
    print(users[0].password)
    serializer=CustomUserSerializer(users, many=True) 
    return Response(serializer.data)      


#####################post section
@api_view(['GET'])
def fetchProfile(request,tkn):
    user=CustomUser.objects.get(token=tkn)
    posts=Post.objects.filter(user=user)
    serializer=PostSerializer(posts,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def fetchFeed(request):
    feeds=Post.objects.all()
    for i in feeds:
        print(i.location)
        print(i.user.name)
    serializer=PostSerializer(feeds,many=True)
    return Response(serializer.data)