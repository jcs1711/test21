from django.shortcuts import render
from django.views.generic import ListView
from .models import Executives

# Create your views here.

class Greeting(ListView):
    model = Executives
    template_name = 'hcgp/greeting.html'

def organization(request):
    return render(request, 'hcgp/orgchart.html')

class Executives(ListView):
    model = Executives
    template_name = 'hcgp/execlist.html'

class HcgpMembers(ListView):
    model = Executives
    template_name = 'hcgp/hmembers.html'

def map(request):
    return render(request, 'hcgp/map.html')




# def blog(request):
    # return render(request, 'main/blog.html')

