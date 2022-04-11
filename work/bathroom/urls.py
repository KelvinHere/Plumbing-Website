from django.urls import path
from . import views

urlpatterns = [
    path('', views.bathroom, name='bathroom'),
]