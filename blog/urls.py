from django.urls import path 
from blog.views import  BlogList,CreateBlog,BlogDetail,UpdateBlog, DeleteBlog

app_name = 'blog'

urlpatterns = [
    path('',BlogList.as_view(), name='blog-list'),
    path('create/',CreateBlog.as_view(),name='create-blog'),
    path('<int:pk>/',BlogDetail.as_view(), name='detail-blog'),
    path('<int:pk>/update/',UpdateBlog.as_view(), name='update-blog'),
    path('<int:pk>/delte/',DeleteBlog.as_view(), name='delete-blog'),

    
]