from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import RequestForm
from .models import Request
from django.http import HttpResponseRedirect, HttpResponseNotFound
from datetime import datetime
from django.core.mail import EmailMessage
import json
from django.core.exceptions import ValidationError

# global variables that will be used throughout views.py
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
json_dates = {}
json_all_dates = {}

def get_dates_for_user(requests_by_name):
    """
    """
        list_of_dates = []
        datetimes = []
        for request in requests_by_name:
            list_of_dates.append((request['date'].encode('ascii'), (request['reservation'].encode('ascii'))))
         
        for date in list_of_dates:
            dateString = datetime.now()
            strings_from_db = date[0].split()
            print strings_from_db
            print months.index(strings_from_db[1]) + 1
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
    global json_all_dates
    dates_list = []
    all_of_the_dates_as_list_of_strings = []

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
        true_date = request.POST.get(datetime.now())
        # a_datetime = datetime.now()
        # words = date.split()
        # the_day_requested = int(words[2])
        # the_month_requested = months.index(words[1]) + 1
        # the_year_requested = int(words[3])
        # print "PRINTING TOKENS"
        # print the_day_requested
        # print the_month_requested
        # print the_year_requested
        # a_datetime.replace(year=the_year_requested)
        # a_datetime.replace(month=the_month_requested)
        # a_datetime.replace(day=the_day_requested)
        # new_string = str(the_day_requested) + words[1] + words[3]
        # b_datetime = datetime.strptime(new_string, '%d%b%Y')
        # print "THE NEW DATETIME"
        # print b_datetime
        # true_date = request.POST.get(b_datetime)
        #post_mutable = request.POST.copy()
        # Now you can change values:
        #post_mutable['true_date'] = b_datetime
        
    
        if form.is_valid():
            form.save()
            requests_by_name = Request.objects.all().filter(full_name=str(full_name)).values()
            requests_by_given_time = Request.objects.all().filter(date=str(date), reservation=str(reservation)).values()
            dates_list = get_dates_for_user(requests_by_name)
            dates_dict = {}
            dstr = 'date'
            for i, date in enumerate(dates_list):
                dates_dict[(dstr + str(i))] = dates_list[i]
            json_dates = json.dumps(dates_dict)
            return HttpResponseRedirect('/thanks')
        
    else: 
        form = RequestForm()

    # This is where I render the rekt.html template on page-load
    all_requests = Request.objects.all().values()
    print all_requests
    all_of_the_dates_as_list_of_strings = get_dates_for_user(all_requests)
    all_dates_dict = {}
    all_dstr = 'date'
    for i, date in enumerate(all_of_the_dates_as_list_of_strings):
        all_dates_dict[(all_dstr + str(i))] = all_of_the_dates_as_list_of_strings[i]
    json_all_dates = json.dumps(all_dates_dict)
    return render(request, 'rekt.html', {'all_dates_json_strings':json_all_dates})
    
    
def SubmissionView(request):
    return render(request, 'thanks.html', {'dates_json_strings':json_dates})