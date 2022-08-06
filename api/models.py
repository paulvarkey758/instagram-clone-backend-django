from django.db import models

# Create your models here.
class CustomUser(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    username=models.CharField(max_length=20, unique=True)
    password=models.CharField(max_length=20)
    token=models.CharField(max_length=20, unique=True,blank=True)
    profilePic=models.ImageField(upload_to="img/",blank=True, null=True,default="img/default-avatar.jpg")
    bio=models.TextField(blank=True,null=True)


    def __str__(self):
        return self.username

class Post(models.Model):
    location=models.CharField(max_length=20,blank=True,null=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)  
    post=models.ImageField(upload_to="post/")  
    comment=models.TextField(blank=True,null=True)
    