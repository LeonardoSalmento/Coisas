from django.db import models

# Create your models here.

class Profile(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=255, null= False)
    email = models.CharField(max_length=255, null = False)
    address = models.ForeignKey('Address', on_delete = models.CASCADE, related_name = 'my_address')


class Comment(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=255, null= False)
    email = models.CharField(max_length=255, null = False)
    body = models.CharField(max_length=255, null = False)
    postId = models.IntegerField(null=False)

class Post(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    title = models.CharField(max_length=255, null= False)
    body = models.CharField(max_length=255, null = False)
    userId = models.IntegerField(null = False)



class Address(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    street = models.CharField(max_length=255, null= False)
    suite = models.CharField(max_length=255, null= True)
    city = models.CharField(max_length=255, null= False)
    zipcode = models.CharField(max_length=255, null= False)
