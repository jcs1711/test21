from django.shortcuts import render
from django.views.generic import ListView
from .models import GeneMember, MyFamilyStory

# Create your views here.

def genehome(request):
    return render(request, 'genealogy/genehome.html')

class MyFamily(ListView):
    model = GeneMember
    template_name = 'genealogy/myfamily.html'

def myfamilystory(request):
    author = request.POST.get('author')
    title = request.POST.get('title')
    content1 = request.POST('content1')
    content2 = request.POST('content2')
    date_created = request.POST('')
    timestamp = request.POST

    return render(request, 'genealogy/myfamilystory.html')

def myfamilystorycreate(request):
    return render(request, 'genealogy/myfamilystorycreate.html')

def mymotherside(request):
    return render(request, 'genealogy/mymotherside.html')

def myrelatives(request):
    return render(request, 'genealogy/myrelatives.html')

def myfamilypic(request):
    return render(request, 'genealogy/myfamilypic.html')

def myfamilymov(request):
    return render(request, 'genealogy/myfamilymov.html')

