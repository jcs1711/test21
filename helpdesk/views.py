from django.shortcuts import render

# Create your views here.

def sudaninfo(request):
    return render(request, 'main/help-desk/sudan-info.html')