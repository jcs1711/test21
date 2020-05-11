from django.urls import path
from . import views
from .views import BlogView, BlogDetailView, AddBlogView

urlpatterns = [
    path('list/', BlogView.as_view(), name = "blog"),   # function으로 define 했을 경우: path('blog/', views.blog, name = "blog")
    path('view/<int:pk>', BlogDetailView.as_view(), name = "blog_detail"),
    path('add/', AddBlogView.as_view(), name = "blog-add"),
]