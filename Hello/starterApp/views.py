from django.shortcuts import render
from django import forms
from django.core import validators
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, 'starterApp/index.html')
    
    
def register(request):
    return render(request, 'starterApp/register.html', {
    'title': 'Register'
    })
    

class LoginForm(forms.Form):
   username = forms.CharField(label='Username', max_length=100)
   password = forms.CharField(
   widget=forms.PasswordInput(),
   label="Password",
   validators=[
   validators.MaxLengthValidator(limit_value=8, message="Password Must Have A Length Of eight(8) character")
   ]
   )
def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        
        if login_form.is_valid():
            return HttpResponseRedirect(reverse("index"))
    else:
        login_form = LoginForm()
    
    return render(request, 'starterApp/login.html', {
    'forms':  login_form
    })