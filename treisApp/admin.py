from ast import Pass
from cgitb import html
from hashlib import shake_128
from http.client import HTTPResponse
from urllib import request
from django.contrib import admin
from treisApp.models import Student,Marks,User
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display= ('name','fathername','dob','academicyear','year','group','address','user')
    list_filter = ('user','group','year')

class MarksAdmin(admin.ModelAdmin):
    list_display = ('name','year','group','testtype','s1','s2','s3','s4','s5','s6','Total','Result','Avg','user')
    list_filter = ('user','year','group','testtype')

    
    '''
    It is working but we need to think about the Title of the Subject.
    '''
    '''
    def Botany(self,request):
        if request.group == 'BPC':
            return request.s3
    '''
    def Total(self,request):
        return request.s1+request.s2+request.s3+request.s4+request.s5+request.s6
    
    def Avg(self,request):
        if request.group == 'MPC' and request.year == 'I year' or request.year == 'II year':
            return round(((request.s1+request.s2+request.s3+request.s4+request.s5+request.s6)/470)*100,2)
        elif request.group == 'BPC' and request.year == 'I year' or request.year == 'II year':
            return round(((request.s1+request.s2+request.s3+request.s4+request.s5+request.s6)/430)*100,2)
        else:            
            return round(((request.s1+request.s2+request.s3+request.s4+request.s5+request.s6)/500)*100,2)

    def Result(self,request):
        if request.group == 'MPC':
            if request.s1>=(35/100*100) and request.s2>=(35/100*100) and request.s3>=(35/100*75) and request.s4>=(35/100*75) and request.s5>=(35/100*60) and request.s1>=(35/100*60):
                return 'Pass'
            else:
                return 'Fail'
        elif request.group == 'BPC':
            if request.s1>=(35/100*100) and request.s2>=(35/100*100) and request.s3>=(35/100*60) and request.s4>=(35/100*60) and request.s5>=(35/100*60) and request.s1>=(35/100*60):
                return 'Pass'
            else:
                return 'Fail'
        elif request.group == 'MEC':
            if request.s1>=(35/100*100) and request.s2>=(35/100*100) and request.s3>=(35/100*100) and request.s4>=(35/100*100) and request.s5>=(35/100*100) and request.s1>=(35/100*100):
                return 'Pass'
            else:
                return 'Fail'

admin.site.register(Student,StudentAdmin)
admin.site.register(Marks,MarksAdmin)

