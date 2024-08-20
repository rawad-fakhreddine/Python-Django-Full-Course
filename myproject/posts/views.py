from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def posts_list(request):
    posts=Post.objects.all().order_by('-date')
    return render(request,'posts/posts_list.html',
    {'posts':posts})
#alt + z

def post_page(request,slug):
    post=Post.objects.get(slug=slug)
    return render(request,'posts/post_page.html',
    {'post':post})


#! If you are not login, so the page in "new post" will appear the login page
@login_required(login_url="/users/login/")
def post_new(request):
    return render(request,'posts/post-new.html')