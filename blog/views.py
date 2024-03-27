from django.shortcuts import render
from .models import Category, Blog
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.views import View


def blog_list(request):
    blogs = Blog.objects.all()
    context = {
            'blogs' : blogs
        }
    return render(request, 'blog/blogList.html', context)


class BlogListView(View):
    
    def get(self, request):
        blogs = Blog.objects.all()
        context = {
            'blogs' : blogs
        }
        return render(request, 'blog/blogList.html', context)
        

class BlogListView(View):
    
    def get(self, request):
        blogs = Blog.objects.all()
        context = {
            'blogs' : blogs
        }
        return render(request, 'blog/blogList.html', context)

