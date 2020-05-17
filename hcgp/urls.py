from django.urls import path
from . import views
from .views import Greeting, Executives, HcgpMembers


urlpatterns = [
    path('greeting/', Greeting.as_view(), name = "greeting"),
    path('organization', views.organization, name = "organization"),
    path('executives/', Executives.as_view(), name = "executives"),
    path('members/', HcgpMembers.as_view(), name = "hmembers"),
    path('map/', views.map, name = "map"),
]