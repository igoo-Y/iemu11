from typing import List
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from . import models


class PostCreateView(CreateView):
    template_name = "posts/post_create.html"
    model = models.Post


class PostListView(ListView):
    model = models.Post
    template_name = "posts/post_list.html"
