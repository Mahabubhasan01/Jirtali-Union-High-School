from django.urls import path
from . import views
urlpatterns = [
    path('attendance-list', views.Attendance_list, name='attendance_list')
]
