from django.shortcuts import render, redirect
from .models import BookATable
from .forms import BookATableForm
import json

def home(request):
    context = {
        "text": "Opening Times",
        "mylist": ["Monday - Friday: 11:00 - 22:00", "Saturday : 17:00 - 22:30", "Sunday : 17:00 - 20:30"],
        "link": "Make your resevration!",
    }
    return render(request, "Booking/home.html", context )     

def booking(request):
    context = { "form": BookATableForm }
    return render(request, "Booking/booking.html", context )  

def addBooking(request):
    form = BookATableForm(request.POST)
 
    if form.is_valid():
        booking = BookATable(
            date = form.cleaned_data['date'],
            time = form.cleaned_data['time'],
            person = form.cleaned_data['person'],
            name = form.cleaned_data['name'], 
            email = form.cleaned_data['email'],
            phone = form.cleaned_data['phone'],
            s_request = form.cleaned_data['s_request'],)
        booking.save()

    return redirect('details')

# redirect user to the latest booking which they have just made
def booking_details(request):
    obj = BookATable.objects.latest('id')
    context = {
        "object": obj
    }
    return render(request, "Booking/booking_details.html", context )  

    
def about(request):
    context = {}
    return render(request, "Booking/about.html", context) 


def contact(request):
    context = {}
    return render(request, "Booking/contact.html", context)     


def menu(request):
    context = { }
    return render(request, "Booking/menu.html", context) 