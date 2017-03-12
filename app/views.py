from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .forms import NameForm

def get_name(request):
    # If this is a POST request, we will need to process the form date
    if request.method == 'POST':
        form = NameForm( request.POST )
        if form.is_valid():
            return HttpResponseRedirect('/your-name/thanks/')
    else:
        form = NameForm()
    return render(request, 'app/name.html', {'form':form})

def thanks(request):
    return HttpResponse('Thanks !')
