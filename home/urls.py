
from django.contrib import admin
from django.urls import path, include 
from .import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls', namespace='account')),
    path('blog/',include('blog.urls',namespace='blog')),

    path('',views.BlogList.as_view(),name='blog-list'),
    

]
