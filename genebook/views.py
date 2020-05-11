from django.shortcuts import render
from django.views.generic import ListView
from .models import GeneMember

# Create your views here.

class GeneBook(ListView):
    model = GeneMember
    template_name = 'genebook/mygene'