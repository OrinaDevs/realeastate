from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/<int:pk>/', views.property_detail, name='property_detail'),
]
