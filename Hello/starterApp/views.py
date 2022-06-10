from django.shortcuts import render
from django import forms

# Create your views here.
def index(request):
    return render(request, 'starterApp/index.html')
    
    
def register(request):
    return render(request, 'starterApp/register.html', {
    'title': 'Register'
    })
    

class LoginForm(forms.Form):
    email = forms.EmailField()
  
def login(request):
    return render(request, 'starterApp/login.html', {
    'forms': LoginForm(request.post)
    })