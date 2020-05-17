from django.urls import path
from .views import ConfirmName
from . import views

urlpatterns = [
    path('', views.help, name = "help"),
    path('sudan-info/', views.sudaninfo, name = "sudan_info"),
    path('confirm-name/', ConfirmName.as_view(), name = "confirm-name"),
]

