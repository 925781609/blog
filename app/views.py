from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .forms import NameForm
from .admin import UserCreationForm 

def get_name(request):
    # If this is a POST request, we will need to process the form date
    if request.method == 'POST':
        form = NameForm( request.POST )
        if form.is_valid():
            return HttpResponseRedirect('/app/test/')
    else:
        form = NameForm()
    return render(request, 'app/name.html', {'form':form})

def register(request):
    print(' 1before form is saved')
    if request.method == 'POST':
        form = UserCreationForm( request.POST )
        print('2 before form is saved')
        if form.is_valid():
            print('***form is saved')
            form.save()
            print('***form is saved')
            return HttpResponseRedirect('/app/test/')
    else:
        form = UserCreationForm()
    return render(request, 'app/name.html', {'form':form})

def test( request ):
    return HttpResponse("Hello test")
