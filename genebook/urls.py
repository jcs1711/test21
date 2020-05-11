from django.urls import path
from .views import GeneBook



urlpatterns = [
    path('genehome/', GeneBook.as_view(), name = "genehome"),
]
