from django.db import models

import datetime
from django.db import models
from django.utils import timezone
from .choices import *
#from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


class BookATable(models.Model):
    date = models.DateField('date')
    time = models.CharField(max_length=5, choices=TIME_SELECT)
    person = models.IntegerField(default=0, choices=PERSON_SELECT)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70)
    #phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    #phone = PhoneNumberField()
    #phone = models.IntegerField(max_length=10)
    phone = models.IntegerField(
        validators=[
            MaxValueValidator(9999999999), 
            MinValueValidator(11111111)
            ])
    s_request = models.CharField(
        verbose_name="Special Request", 
        max_length=1024, 
        null=True, 
        blank=True)
    
    def __str__(self):
        # return self.name 
        # return 'Booking: ' + self.name
        return 'Name: {}, phone: {}, date: {}, time: {}, person: {}'.format(
            self.name, self.phone, self.date, self.time, self.person)



