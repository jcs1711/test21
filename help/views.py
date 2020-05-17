from django.shortcuts import render
from django.views.generic import ListView
from .models import JMembers

# Create your views here.

def help(request):
    return render(request, 'main/help/help.html')

def sudaninfo(request):
    return render(request, 'main/help/sudan-info.html')

class ConfirmName(ListView):
    model = JMembers
    template_name = 'main/help/confirmname.html'

