from django.urls import path

from . import views

urlpatterns = [ 
    path('home', views.home),
    path('new_function/', views.new_function)
]