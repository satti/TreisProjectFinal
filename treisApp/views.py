from django.http import HttpResponse, request
from django.http import response
from django.shortcuts import render,redirect
from .forms import StudentForm,loginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Marks, Student
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from copy import deepcopy
from django.contrib import messages
# Create your views here.

def loginView(request):
    #form = loginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse('User Not Exist')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(homeView)
    else:
        return render(request,'login.html',{})
def logoutPage(request):
    logout(request)
    return redirect(homeView)

def studentView(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        name = request.POST['name']
        fathername = request.POST['fathername']
        dob = request.POST['dob']
        ac = '21'
        year = request.POST['year']
        group = request.POST['group']
        address = request.POST['address']
        Student.objects.create(user=user,name=name,fathername=fathername,dob=dob,academicyear=ac,year=year,group=group,address=address)
        messages.info(request,"Student Data Inserted")
        return redirect(homeView)         
    else:
        return render(request,'student.html',{})


def students(request):
    if request.method == 'POST':
        y = request.POST.get('year')
        g = request.POST.get('group')
        print(y,g,request.user.id)
        students = Student.objects.filter(year=y, group=g, user_id=request.user.id).order_by('id')
        #stu = deepcopy(students)
        print(students.count())
        if students:
            p = Paginator(students,2)
            #page_request_var = "page"
            page_number = request.session.get('pa')
            #print('page_number',page_number)
            #print()
            #page_obj = p.get_page(page_number)
            try:
                page_obj = p.get_page(page_number)
            except PageNotAnInteger:
                page_obj = p.page(1)
            except EmptyPage:
                page_obj = p.page(p.num_pages)
            #-context = {'page_obj': page_obj,'page_request_var':page_request_var}
            #print(dir(p))
            #print('page')
            return render(request,'studentslist.html',{'students':students,'page_obj':page_obj})
    else:
        request.session['pa']=1
        return render(request,'student_display.html',{})

'''
def studentList(request):
    if request.method == 'GET':
        y = request.GET.get('year')
        g = request.GET.get('group')
        print(y,g,request.user.id)
        students = Student.objects.filter(year=y, group=g, user_id=request.user.id)
        stu = deepcopy(students)
        p = Paginator(stu,3)
        page_request_var = "page"
        page_number = request.GET.get('page_request_var')
        print(page_number)
        page_obj = p.get_page(page_number)
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)
        context = {'page_obj': page_obj,
        'page_request_var':page_request_var}
        #print(dir(p))
        print(request.GET)
        #print(page_obj.object_list)
        print(p.num_pages)
        print(y)
        print(students)
        return render(request,'studentslist.html',{'students':students})
        #return render(request,'studentslist.html',context)

'''
def homeView(request):
    return render(request,'home.html',{})
def marksView(request):
    return render(request,"studentsmarks.html",{})

def marksEntry(request):
    form = Student.objects.filter(user_id=request.user.id, year=request.GET.get('year'),
    group=request.GET.get('group'))
    if request.method == 'POST':
        for i in range(1,len(form)+1):
            name = form[i-1]
            user = User.objects.get(id=request.user.id)
            year = request.GET.get('year')
            group = request.GET.get('group')
            test = request.GET.get('test')
            ac = Student.objects.filter(user_id=request.user.id).values()[0]['academicyear']
            print(ac)
            if group == 'MPC':
                E = request.POST.get('E'+str(i)+'')
                S = request.POST.get('S'+str(i)+'')
                MA = request.POST.get('MA'+str(i)+'')
                MB = request.POST.get('MB'+str(i)+'')
                P = request.POST.get('P'+str(i)+'')
                C = request.POST.get('C'+str(i)+'')
                Marks.objects.create(name=name,user=user,year=year,group=group,testtype=test,ac=ac,s1=E,s2=S,s3=MA,s4=MB,s5=P,s6=C)
            elif group == 'BPC':
                E = request.POST.get('E'+str(i)+'')
                S = request.POST.get('S'+str(i)+'')
                MA = request.POST.get('BO'+str(i)+'')
                MB = request.POST.get('ZO'+str(i)+'')
                P = request.POST.get('BP'+str(i)+'')
                C = request.POST.get('BC'+str(i)+'')
                Marks.objects.create(name=name,user=user,year=year,group=group,testtype=test,ac=ac,s1=E,s2=S,s3=MA,s4=MB,s5=P,s6=C)
            else:   
                E = request.POST.get('E'+str(i)+'')
                S = request.POST.get('S'+str(i)+'')
                MA = request.POST.get('EMA'+str(i)+'')
                MB = request.POST.get('EMB'+str(i)+'')
                P = request.POST.get('ECO'+str(i)+'')
                C = request.POST.get('COMM'+str(i)+'')
                Marks.objects.create(name=name,user=user,year=year,group=group,testtype=test,ac=ac,s1=E,s2=S,s3=MA,s4=MB,s5=P,s6=C)
        messages.info(request,f"Marks of {year} {group} {test} Inserted Successfully!")        
        return redirect(homeView)
    else:
        g = request.GET.get('group')
        if Marks.objects.filter(user_id=request.user.id,group=request.GET.get('group'),testtype=request.GET.get('test'),
        year=request.GET.get('year')):
            return render(request,'marksalreadyentered.html',{})
        elif g =='MPC': 
            return render(request,'marks.html',{'form':form})
        elif g =='BPC':
            return render(request,'marksbpc.html',{'form':form})
        else:
            return render(request,'marksmec.html',{'form':form})  
'''
def marksReport(request):
    if request.method =="GET":
        y = request.GET.get('year')
        g = request.GET.get('group')
        type = request.GET.get('testtype')
        report = Marks.objects.filter(user_id=request.user.id,year=y,group=g,testtype=type)
    return render(request,'marksreport.html',{'report':report})
'''


def marksList(request):
    if request.method =="POST":
        y = request.POST.get('year')
        g = request.POST.get('group')
        type = request.POST.get('testtype')
        report = Marks.objects.filter(user_id=request.user.id,year=y,group=g,testtype=type)
        if g =='MPC':
            return render(request,'marksreport.html',{'report':report})
        elif g == 'BPC':
            return render(request,'marksreportbpc.html',{'report':report})
        else:
            return render(request,'marksreportmec.html',{'report':report})
    else:
        return render(request,'markslist.html',{})


def update_student_view(request,pk):
    form = Student.objects.get(id=pk)
    if request.method =='POST':
        form.name = request.POST.get('name')
        form.fathername = request.POST.get('fathername')
        form.dob = request.POST.get('dob')
        form.year = request.POST.get('year')
        form.group = request.POST.get('group')
        form.address = request.POST.get('address')
        form.save()
        return render(request,'studentdetailsupdate.html',{})
    else:
        return render(request,'studentupdate.html',{'form':form})

def student_delete(request,pk):
    form = Student.objects.get(id=pk)
    form.delete()
    return render(request,'studentdelete.html',{})


