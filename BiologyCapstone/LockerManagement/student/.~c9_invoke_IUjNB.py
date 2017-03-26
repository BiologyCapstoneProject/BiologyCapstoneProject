from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .models import Request

def index(request):
    print 'WORKED'
    print '\n\nWENT THROUGH'
    form = PostForm(request.POST or None)
    print '\n\nWENT THROUGH'
        instance = form.save(commit=False)
        instance.save()
        print 'Request', request.POST.get("date")
        
    context = {
        "form": form,
    }
    #return render(request, "rekt.html", context)
    
    
    