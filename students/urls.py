from django.urls import path
from . import views
urlpatterns = [
    path('', views.Students_list, name='students_list')
]
