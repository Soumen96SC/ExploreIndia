from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    
    path("book", v.booking, name='book'),
    path("home", v.index),
    path("DestinationDetails/<int:id>/", v.destinationview),
    path("About", v.aboutpage),
    path("search", v.search),
    path("Destinations", v.traveldest),
    path("mybookings", v.mybookings, name='bookinghistory'),
    path("bookingDetails", v.booking_details, name='bookingDetails'),
    path("cancelbooking", v.cancel_booking, name='cancelbooking'),
    
   
]
