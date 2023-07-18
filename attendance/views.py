from django.shortcuts import render

# Create your views here.
def Attendance_list(request):
    return render(request,'attendance_list.html')