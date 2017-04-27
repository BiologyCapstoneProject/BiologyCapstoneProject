from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import RequestForm
from .models import Request
from django.http import HttpResponseRedirect, HttpResponseNotFound
from datetime import datetime
from django.core.mail import EmailMessage
import json
from django.core.exceptions import ValidationError


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
json_dates = {}
def get_dates_for_user(requests_by_name):
        list_of_dates = []
        datetimes = []
        for request in requests_by_name:
            list_of_dates.append((request['date'].encode('ascii'), (request['reservation'].encode('ascii'))))
         
        for date in list_of_dates:
            dateString = datetime.now()
            strings_from_db = date[0].split()
            newDate = dateString.replace(month = months.index(strings_from_db[1]) + 1, 
            day = int(strings_from_db[2]), 
            year =  int(strings_from_db[3]),
            hour = int(date[1][0]))
            datetimes.append(newDate)    
            
        datetimes = sorted(datetimes)
        strings_to_ship = []
        minute = '00'
        meridian = 'AM'
        for date in datetimes:
            if date.hour is 8:
                minute = '30'
                meridian = 'AM'
            else:
                minute = '00'
                meridian = 'PM'
            string_to_ship = days[date.weekday()] + ' ' + months[date.month - 1] + ' ' + str(date.day) + ' ' + str(date.year) + ' ' + str(date.hour) + ':' + minute + ' ' +  meridian  
            strings_to_ship.append(string_to_ship)
            
        return strings_to_ship

def RequestView(request):
    global json_dates
    dates_list = []

    if request.method == 'POST':
        # email = EmailMessage('Hello everyone', 'World', to=['nghaberman@gmail.com'])
        # email.send()
        
        form = RequestForm(data=request.POST)
        date = request.POST.get('date', '')
        reservation = request.POST.get('reservation', '')
        full_name = request.POST.get('full_name', '')
        email = request.POST.get('email', '')
        phone_num = request.POST.get('phone_num', '')
        timestamp = request.POST.get(datetime.now())
        true_date = request.POST.get(date)
        
        print
        if form.is_valid():
            form.save()
            requests_by_name = Request.objects.all().filter(full_name=str(full_name)).values()
            requests_by_given_time = Request.objects.all().filter(date=str(date), reservation=str(reservation)).values()
            dates_list = get_dates_for_user(requests_by_name)
            #json_dates = json.dumps(requests_by_name[0])
            dates_dict = {}
            dstr = 'date'
            for i, date in enumerate(dates_list):
                dates_dict[(dstr + str(i))] = dates_list[i]
            json_dates = json.dumps(dates_dict)
                
            count_am = 0
            count_pm = 0
            for request in requests_by_given_time:
                if request['reservation'].encode('ascii')[0] is '8':
                    count_am += 1
                else:
                    count_pm += 1
            # if there are now 4 requests for the given date:
            # disable that date in the calendar
                
            
            return HttpResponseRedirect('/thanks')
        
    else: 
        form = RequestForm()
    #return render(request, 'rekt.html', {'dates_list': dates_list})

    return render(request, 'rekt.html')
    
    
def SubmissionView(request):
    #return render(request, 'thanks.html')
    return render(request, 'thanks.html', {'dates_json_strings':json_dates})