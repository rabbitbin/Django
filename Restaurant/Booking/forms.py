import datetime
from django import forms
from django.utils import timezone 
from .choices import *
#from phonenumber_field.formfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator 

class BookATableForm(forms.Form):
    date = forms.DateField(
        widget=forms.TextInput(
        attrs={'class':'input-group date form-control datepicker'}))    
    time = forms.CharField(
        widget=forms.Select(choices=TIME_SELECT, 
        attrs={'class':'custom-select mr-sm-2', 'id':'inlineFormCustomSelect'}))
    person = forms.IntegerField(
        widget=forms.Select(choices=PERSON_SELECT, 
        attrs={'class':'custom-select mr-sm-2', 'id':'inlineFormCustomSelect'}))
    name = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    email = forms.EmailField(max_length=70,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'E-mail'}))
    phone = forms.IntegerField(validators=[
        MaxValueValidator(9999999999), 
        MinValueValidator(11111111)],
        help_text='<br>Please entry minuium 8 digital number!',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Phone'}))
    #phone = forms.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    #phone = forms.IntegerField(label='Your phone')
    #phone = forms.CharField(label='Phone', max_length=15)
    #phone = PhoneNumberField()
    #phone = PhoneNumber.from_string(phone_number=raw_phone, region='SE').as_e164
    s_request = forms.CharField(label='Special Request', 
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Special Request'}), 
        required=False)

