from django.contrib import admin
from .models import Category, Blog


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name']


class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category', 'create_time', 'update_time']
    

admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Blog, BlogModelAdmin)

