from unicodedata import name
from django.shortcuts import render

# Create your views here.


def Published_Results(request):
    return render(request, 'publishedresults.html')
