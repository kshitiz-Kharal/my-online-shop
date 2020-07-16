from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('blogpost/<int:myid>', views.blogpost, name="blogpost"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
]