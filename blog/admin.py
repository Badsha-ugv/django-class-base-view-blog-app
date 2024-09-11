from django.contrib import admin

from .models import Blog

class BlogAdmin(admin.ModelAdmin):

    list_display = ['title', 'created', 'is_published']
    list_filter = ['created', 'is_published']
    search_fields = ['title',]

admin.site.register(Blog, BlogAdmin)