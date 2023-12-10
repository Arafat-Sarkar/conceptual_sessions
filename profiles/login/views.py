from django.shortcuts import render
from .import forms
# Create your views here.

def loginHome(request):
    if request.method=="POST":
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        return render (request, 'login_home.html' ,{'name': name,'email': email})
    
    else:
        return render (request, 'login_home.html' )

def Bform(request):
    return render (request, 'B_form.html' )

def Dform(request):
    form= forms.djangoForm()
    return render (request, 'django_form.html', {'form': form})
    
  
    