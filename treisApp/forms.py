from dataclasses import fields
from logging import PlaceHolder
from multiprocessing.sharedctypes import Value
#from tkinter import Widget
from django.contrib.auth.models import User
from django import forms
from django.forms import HiddenInput, ModelForm,DateInput, PasswordInput, widgets
from django.http import request
from .models import Student

class DateInput(forms.DateInput):
    input_type = 'date'


class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['user']
        widgets = {
            'dob': DateInput()
        } 
class loginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'password': PasswordInput(),
        }
        