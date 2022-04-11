from django.urls import path
from . import views

urlpatterns = [
    path('', views.heating, name='heating'),
    path('heatingspares', views.heatingspares, name='heatingspares'),
    path('heatpumps', views.heatpumps, name='heatpumps'),
    path('renewables', views.renewables, name='renewables'),
    path('stoves', views.stoves, name='stoves'),
]