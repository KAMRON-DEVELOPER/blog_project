from django.shortcuts import render
from .models import Category, Blog
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.views import View


def blog_list(request):
    blogs = Blog.objects.all()
    users = User.objects.all()
    context = {
            'blogs' : blogs,
            'users' : users
        }
    return render(request, 'blog/blogList.html', context)


class BlogListView(View):
    
    def get(self, request):
        blogs = Blog.objects.all()
        users = User.objects.all()
        print(len(users))
        context = {
            'blogs' : blogs,
            'users' : users
        }
        return render(request, 'blog/blogList.html', context)
        

class BlogDetailView(View):
    
    def get(self, request, id):
        blogs = Blog.objects.all()
        users = User.objects.all()
        blog = Blog.objects.get(id=id)
        context = {
            'blogs' : blogs,
            'users' : users,
            'blog' : blog
        }
        return render(request, 'blog/blogDetail.html', context)

