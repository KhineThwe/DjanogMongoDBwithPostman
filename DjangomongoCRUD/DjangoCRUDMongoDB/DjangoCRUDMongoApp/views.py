from bson import ObjectId
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .models import Posts

@csrf_exempt
def add_post(request):
	comment = request.POST.get("comments").split(",")
	tags = request.POST.get("tags").split(",")
	user_details ={"first_name":request.POST.get("first_name"),"last_name":request.POST.get("last_name")}
	post = Posts(post_title=request.POST.get("post_title"),post_description=request.POST.get("post_description"),comment = comment,tags=tags,user_details=user_details)
	post.save()
	return HttpResponse('Inserted')

@csrf_exempt
def update_post(request,id):
	post = Posts.objects.get(_id=ObjectId(id))
	post.user_details["first_name"] = request.POST.get("first_name")
	post.save()
	return HttpResponse('Post Updated')

@csrf_exempt
def delete_post(request,id):
	post = Posts.objects.get(_id=ObjectId(id))
	post.delete()
	return HttpResponse('Post Deleted')

def read_one_post(request,id):
	post = Posts.objects.get(_id=ObjectId(id))
	stringVal = "First Name"+post.user_details["first_name"]+"Last Name"+post.user_details["last_name"]+"Post Title"+post.post_title+"Comments"+post.comment[0]
	return HttpResponse(stringVal)

def read_all_post(request):
	posts = Posts.objects.all()
	stringVal = ""
	for post in posts:
		stringVal = "First Name" + post.user_details["first_name"] + "Last Name" + post.user_details[
			"last_name"] + "Post Title" + post.post_title + "Comments" + post.comment[0]
	return HttpResponse(stringVal)
	
	
