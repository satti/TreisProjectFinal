from datetime import date
from operator import mod
from os import access
from random import choices
from unicodedata import name
#from tkinter import CASCADE, CURRENT
from django.contrib.auth.models import User
from django.db import models
from django.http import request

class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    fathername = models.CharField(max_length=200,null=True)
    dob = models.DateField(null=True)
    ay = (('21','2021-2022'),
            ('22','2022-2023'),
            ('23','2023-2024'),)
    academicyear = models.CharField(max_length=100, choices = ay, default='2021-2022',null=True)
    y = (('I Year', 'I Year'),
                ('II Year','II Year'),)
    year = models.CharField(max_length=50,choices=y, null=True)
    g = (('MPC','MPC'),
        ('BPC','BPC'),
        ('MEC','MEC'),)
    group = models.CharField(max_length=100,choices=g,null=True)
    address = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name
class Marks(models.Model):
    name = models.ForeignKey(Student,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    year = models.CharField(max_length=100,null=True)
    group = models.CharField(max_length=100,null=True)
    testtype = models.CharField(max_length=100,null=True)
    ac = models.CharField(max_length=20,null=True)
    s1 = models.IntegerField()
    s2 = models.IntegerField()
    s3 = models.IntegerField()
    s4 = models.IntegerField()
    s5 = models.IntegerField()
    s6 = models.IntegerField()
    def __str__(self):
        return self.name
