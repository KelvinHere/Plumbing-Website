from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('get_modal_data/', views.get_modal_data, name='get_modal_data'),
]