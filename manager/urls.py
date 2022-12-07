from django.urls import path
from manager import views

urlpatterns = [
     path('category', views.category , name='category'),
     path('product', views.product , name='product'),
]