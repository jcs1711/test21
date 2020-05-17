from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'main/index.html')

def help(request):
    return render(request, 'main/help/help.html')

