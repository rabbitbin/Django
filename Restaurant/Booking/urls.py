from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('booking/', views.booking, name = 'booking'),
    path('addBooking/', views.addBooking, name = 'addBooking'),
    path('booking_details/', views.booking_details, name = 'details'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('menu/', views.menu, name = 'menu'),
]

