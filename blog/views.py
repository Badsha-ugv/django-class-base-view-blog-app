from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic 

from .models import Blog


class CreateBlog(generic.CreateView):
    model = Blog
    fields = ['title','description']
    template_name = 'blog/create_blog.html'
    success_url = reverse_lazy('blog-list')

    # def form_valid(self, form):
    #     return super().form_valid(form)

