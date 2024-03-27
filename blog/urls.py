from django.urls import path
from .views import blog_list, BlogListView, BlogDetailView


urlpatterns = [
    path('', BlogListView.as_view(), name='blogs'),
    path('detail/<int:id>/', BlogDetailView.as_view(), name='detail'),
]


