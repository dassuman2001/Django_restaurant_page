from django.http import JsonResponse
from django.shortcuts import redirect, render
# from foodio.forms import BookingForm
from foodio_app.models import Booking
from django.core.mail import send_mail
from Djangofoodio_project import settings
import uuid

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        person_count = request.POST.get('person')

        # Save form data to the database
        reserv = Booking.objects.create(name=name, email=email, mobile=mobile, person_count=person_count)
        reserv.save()

        # email confirmation
        booking_id = uuid.uuid4().hex[:6]  # Generate a random 6-character booking ID
        subject = 'Confirmation: Your Table Booking Succesful'
        message = f'Thank you for your booking!\n\nYour booking deatils -\nBooking ID: {booking_id} \nName: {name}\nNumber of People: {person_count}'
        sender_email = settings.EMAIL_HOST_USER 
        recipient_email = [email]  
        send_mail(subject, message, sender_email, recipient_email,fail_silently=False)
        return redirect('index')
    else:
        return render(request, 'index.html')

