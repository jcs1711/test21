from django.shortcuts import render
from django.views.generic import ListView
from .models import Executives

# Create your views here.

class Greeting(ListView):
    model = Executives
    template_name = 'main/hcgp/greeting.html'




# def blog(request):
    # return render(request, 'main/blog.html')

