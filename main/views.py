from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'main/main.html')

def help(request):
    return render(request, 'main/help-desk/help.html')

def greeting(request):
    return render(request, 'main/hcgp/greeting.html')