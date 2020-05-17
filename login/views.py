from django.shortcuts import render
from django.views.generic import ListView
from .models import HMember

# Create your views here.

def login(request):
    all_hmembers = HMember.objects.all
    return render(request, 'login/login.html', {'all': all_hmembers})

def signup(request):
    return render(request, 'login/signup.html')

def reset(request):
    return render(request, 'login/reset.html')






# class HLogin(ListView):
#    model = 'HMember'


#    def hmlogin(self):
#        if request.method == 'POST':
#            email = request.POST['email']
#            password =request.POST['password']
#       return render(request, 'login/login.html', {})
#    else:
#        return render(request, 'login/login.html', {})

#def signup(request):
#    return render(request, 'login/signup.html')

