from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import RequestForm
from .models import Request
from django.http import HttpResponseRedirect, HttpResponseNotFound


def RequestView(request):
    if request.method == 'POST':
        form = RequestForm(data=request.POST)
        print 'Form: ', form
        print 'Errors', form.errors
        date = request.POST.get('date', '')
        #reservation = request.POST.get('reservation', '')
        #print 'RESERVATION', reservation

        print 'DATE: ', date
        if form.is_valid():
            print "DID WORK"
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("Form Not Valid")
        
        return render(request, 'rekt.html', )
            
    else : 
        form = RequestForm()
    
    return render(request, 'rekt.html')