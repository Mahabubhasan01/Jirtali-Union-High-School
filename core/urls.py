from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('dashboard', views.Dashboard, name='dashboard'),
    path('subjects-manager', views.Subjects_Manager, name='subjects-manager'),
    path('subjects-manager/class_nine_subjects-manager', views.Class_Nine_Subjects_Manager,
         name='cn'),
    path('subjects-manager/class_ten_subjects-manager', views.Class_Ten_Subjects_Manager,
         name='ct'),
    path('subjects', views.Subjects, name='subjects'),
    path('users-manager', views.Users_Manager, name='users'),
    path('staffs-manager', views.Staffs_Manager, name='staffs'),
    path('fees-manager', views.Fees_Manager, name='fees'),
    path('profile', views.User_Profile, name='profile'),
    path('dashboard-home', views.Dashbord_Home, name='dashboard-home'),
    path('', include('attendance.urls'), name='attendance'),
    path('teachers', include('teachers.urls')),
    path('students/', include('students.urls'), name='students'),
    path('exams/', include('exams.urls'), name='exams'),
    path('', include('results.urls'), name='resutls'),
]
