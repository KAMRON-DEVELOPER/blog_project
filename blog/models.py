from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=200)
    author = models.CharField(max_length=200)
    create_time = models.CharField(max_length=200)


