from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import RequestForm
from .models import Request
from django.http import HttpResponseRedirect, HttpResponseNotFound


def RequestView(request):
    if request.method == 'POST':
        print 'DID RETURN'
        form = RequestForm(request.POST)
        date = request.POST.get('date', '')
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("Form Not Valid")
        
           
        return render(request, 'rekt.html', )
            
    else : 
        form = RequestForm()
    
    return render(request, 'rekt.html')