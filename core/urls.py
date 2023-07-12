from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Home),
    path('attendance/', include('attendance.urls'), name='attendance'),
    path('teachers/', include('teachers.urls'), name='teachers'),
    path('students/', include('students.urls'), name='students'),
    path('exams/', include('exams.urls'), name='exams'),
    path('results/', include('results.urls'), name='resutls'),
]
