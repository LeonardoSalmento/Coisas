from apps.models import *
import json


with open("comments.json", "r") as read_file:
    data = json.load(read_file)

with open("users.json", "r") as read_file:
    data1 = json.load(read_file)

with open("posts.json", "r") as read_file:
    data2 = json.load(read_file)        


for i in range(len(data['comments'])):
    comments = Comment()
    comments.body = data['comments'][i]["body"]
    comments.email = data['comments'][i]["email"]
    comments.postId = data['comments'][i]["postId"]
    comments.id = data['comments'][i]["id"]
    comments.name = data['comments'][i]["name"]
    comments.save()

for i in range(len(data2['posts'])):
    posts = Post()
    posts.body = data2['posts'][i]["body"]
    posts.userId = data2['posts'][i]["userId"]
    posts.title = data2['posts'][i]["title"]
    posts.id = data2['posts'][i]["id"]
    posts.save()

for i in range(len(data1['users'])):


	users = Profile()
	users.username = data1['users'][i]["username"]
	users.id = data1['users'][i]["id"]
	users.address = address
	users.email = data1['users'][i]["email"]

	users.save()




"""
address = Address()
address.street = data1["users"][i]["address"]["street"]
address.suite = data1["users"][i]["address"]["suite"]
address.city = data1["users"][i]["address"]["city"]
address.zipcode = data1["users"][i]["address"]["zipcode"]
address.save()"""

