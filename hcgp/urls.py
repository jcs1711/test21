from django.urls import path
from .views import Greeting

urlpatterns = [
    path('greeting/', Greeting.as_view(), name = "greeting"),
]