from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views import generic 

from .models import Blog

class BlogList(generic.ListView):

    model = Blog
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    queryset = Blog.objects.all()

class CreateBlog(generic.CreateView):
    model = Blog
    fields = ['title','description']
    template_name = 'blog/create_blog.html'
    success_url = reverse_lazy('blog:blog-list')

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class BlogDetail(generic.DeleteView):
    model = Blog 
    template_name = 'blog/detail.html'
    context_object_name = 'blog'

class UpdateBlog(generic.UpdateView):
    model = Blog 
    template_name = 'blog/update.html'
    fields = ['title','description']
    success_url = reverse_lazy('blog:blog-list')

    # def form_valid(self, form: BaseModelForm) -> HttpResponse:

    #     return super().form_valid(form)

    # def get_success_url(self):
    #     return super().get_success_url()