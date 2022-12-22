from os import name
from django import views
from .models import Student
from .import views
from django.urls import path
urlpatterns = [
    path('',views.homeView,name='home'),
    path('login/',views.loginView,name='loginview'),
    path('logout/',views.logoutPage,name='logoutpage'),
    path('student/',views.studentView,name='student'),
    path('studReport/',views.students_view,name='studentsreport'),
    path('marks/',views.marksView,name="marksentry"),
    #path('studentlist/',views.studentList,name="studentList"),
    path('marksentry/',views.marksEntry,name="marks"),
    #path('marksreport/',views.marksReport,name="marksreport"),
    path('markslist/',views.marksList,name="markslist"),
    path('studentupdat/<int:pk>/',views.update_student_view,name='studupdate'),
    path('studentdelete/<int:pk>/',views.student_delete,name='studentdelete'),
]