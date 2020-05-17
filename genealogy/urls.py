from django.urls import path
from . import views
from .views import MyFamily


urlpatterns = [
    path('', views.genehome, name = "genehome"),
    path('myfamily/', MyFamily.as_view(), name = "my_family"),
    path('myfamilystory/', views.myfamilystory, name = "my_family_story"),
    path('myfamilystory/create/', views.myfamilystorycreate, name = "my_family_story_create"),
    path('mymotherside/', views.mymotherside, name = "my_mother_side"),
    path('myrelatives/', views.myrelatives, name = "my_relatives"),
    path('myfamilypic/', views.myfamilypic, name = "my_family_pic"),
    path('myfamilymov/', views.myfamilymov, name = "my_family_mov"),
]
