from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('dashboard', views.Dashboard, name='dashboard'),
    path('dashboard-home', views.Dashbord_Home, name='dashboard-home'),
    path('attendance/', include('attendance.urls'), name='attendance'),
    path('teachers', include('teachers.urls')),
    path('students/', include('students.urls'), name='students'),
    path('exams/', include('exams.urls'), name='exams'),
    path('results/', include('results.urls'), name='resutls'),
]
