from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.

# def blog(request):
    # return render(request, 'main/blog.html')

class BlogView(ListView):
    model = Post
    template_name = 'main/blog/blog.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'main/blog/blog_details.html'

class AddBlogView(CreateView):
    model = Post
    template_name = 'main/blog/add_blog.html'
    fields = '__all__'   # all fields of Post in models.py
