
from django.shortcuts import render


from django.views import generic 
from blog.models import Blog

class BlogList(generic.ListView):

    model = Blog
    template_name = 'home/list.html'
    context_object_name = 'posts'
    queryset = Blog.objects.all()