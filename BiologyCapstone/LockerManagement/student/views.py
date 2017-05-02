"""
Switchs between views and renders the html pages.
"""

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
    """ Takes a list of dictionaries from the database as an argument
    
        Creates a list of datetime objects, one for each date/reservation in the database
        Sorts the list of datetime objects
        Converts list of datetime objects to a list of String representation of dates
        
        Returns: a list of String representations of dates, ready to be shipped back to the front-end
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
    """Renders the form and grabs data from the 
        UI.
    """
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
    
        if form.is_valid():
            form.save()
            # a list of dictionaries containing all records in the database for the input full_name
            requests_by_name = Request.objects.all().filter(full_name=str(full_name)).values()
            # a list of dictionaries containing all records in the database. Each dictionary has a date and a reservation
            requests_by_given_time = Request.objects.all().filter(date=str(date), reservation=str(reservation)).values()
            dates_list = get_dates_for_user(requests_by_name)
            dates_dict = {}
            dstr = 'date'
            # create a dictionary that can be dumped into a json and shipped to the front-end
            for i, date in enumerate(dates_list):
                dates_dict[(dstr + str(i))] = dates_list[i]
            json_dates = json.dumps(dates_dict)
            return HttpResponseRedirect('/thanks')
        
    else: 
        form = RequestForm()

    # This is where we render the rekt.html template on page-load
    all_requests = Request.objects.all().values()
    print all_requests
    all_of_the_dates_as_list_of_strings = get_dates_for_user(all_requests)
    all_dates_dict = {}
    all_dstr = 'date'
    # create a dictionary that can be dumped inot a json and shipped to the front-end
    for i, date in enumerate(all_of_the_dates_as_list_of_strings):
        all_dates_dict[(all_dstr + str(i))] = all_of_the_dates_as_list_of_strings[i]
    json_all_dates = json.dumps(all_dates_dict)
    return render(request, 'rekt.html', {'all_dates_json_strings':json_all_dates})
    
    
def SubmissionView(request):
    """
    Renders the thank you page on submission.
    """
    return render(request, 'thanks.html', {'dates_json_strings':json_dates})