from django.urls import path
from . import views
urlpatterns = [
    path('published-results', views.Published_Results, name='published-results')
]
