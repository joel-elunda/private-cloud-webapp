from django.shortcuts import render
from user.forms import UserLogin
from django.urls import reverse

def home(request):
    form = UserLogin()
    return render(request, 'main.html' )
