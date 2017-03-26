from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .models import Request

    print 'wORKED'
    print 'WORKED'
    print '\n\nWENT THROUGH'
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print 'Request', request.POST.get("date")
        
    context = {
        "form": form,
    }
    #return render(request, "rekt.html", context)
    
    
    