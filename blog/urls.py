from django.urls import path
from .views import blog_list, BlogListView


urlpatterns = [
    path('', blog_list, name='blog_list')
]


