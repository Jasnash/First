from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from.forms import SignUpForm
from django.contrib import messages
from .models import *
# Create your views here.


def home(request):
    #do something
    records = Record.objects.all()
    return render(request, 'home.html', {'records':records})

def register_user(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

        #authenticate
        username = request.POST('username')
        password = request.POST('password')
        user = authenticate(request, username=username, password=password)

       
        login(request, user)
        return redirect('home')
    else:
        form =SignUpForm()
        return render(request, 'register.html',{'form': form})

    return render(request, 'register.html',{'form': form})