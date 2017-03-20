from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import NameForm, LoginForm
from .admin import UserCreationForm 
from .models import User
from .backends import EmailOrUsernameModelBackend
def get_name(request):
    # If this is a POST request, we will need to process the form date
    if request.method == 'POST':
        form = NameForm( request.POST )
        if form.is_valid():
            return HttpResponseRedirect('/app/test/')
    else:
        form = NameForm()
    return render(request, 'app/test.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm( request.POST )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app/test/')
    else:
        form = UserCreationForm()
    return render(request, 'app/name.html', {'form':form})


def log_in(request):
    if request.method == 'POST':
        loginform = LoginForm( request.POST )
        email_backend = EmailOrUsernameModelBackend() 
        if loginform.is_valid():
            email = loginform.cleaned_data['email']
            password = loginform.cleaned_data['password']
            user =email_backend.authenticate(email, password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/app/test/')
            else:
                pass
    else:
        loginform = LoginForm()
    return render(request, 'app/login.html', {'form': loginform})

@login_required(login_url='/app/login/')
def log_out(request):
    logout(request)
    return render(request, 'app/test.html')


def test( request ):
    return render(request, 'app/test.html')
