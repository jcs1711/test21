from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = "main"),
    path('help/', views.help, name = "help"),
    path('hcgp/', views.greeting, name = "greeting"),
]