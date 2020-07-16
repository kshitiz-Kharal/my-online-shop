from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="About Us"),
    path('contact/', views.contact, name="Contact Us"),
    path('tracker/', views.tracker, name="Tracking status"),
    path('search/', views.search, name="Search"),
    path('products/<int:id>', views.productview, name="ProductView"),
    path('checkout/', views.checkout, name="Checkout"),
    # path('handlerequest/', views.handlerequest, name="hadlerequest"),
]
