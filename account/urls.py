from django.urls import path 
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='loign'),
    

]