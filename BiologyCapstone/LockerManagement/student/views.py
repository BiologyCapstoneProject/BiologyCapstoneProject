from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import RequestForm
from .models import Request
from django.http import HttpResponseRedirect, HttpResponseNotFound
from datetime import datetime

def RequestView(request):
    ### Put time stamp in database
    if request.method == 'POST':
        form = RequestForm(data=request.POST)
        print 'Form: ', form
        print 'Errors', form.errors
        date = request.POST.get('date', '')
        reservation = request.POST.get('reservation', '')
        full_name = request.POST.get('full_name', '')
        timestamp = request.POST.get(datetime.now())
        email = request.POST.get('email', '')
        phone_num = request.POST.get('phone_num', '')
        print 'RESERVATION', reservation
        print 'full_name', full_name
        print 'DATE: ', date
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("Form Not Valid")
        
        return render(request, 'rekt.html', )
            
    else : 
        form = RequestForm()
    
    return render(request, 'rekt.html')
    
