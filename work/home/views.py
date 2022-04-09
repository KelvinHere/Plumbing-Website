from django.shortcuts import render, HttpResponse
from products.models import Product
import json

def home(request):
    request.session['shop_filter'] = 'All'
    template = "home/index.html"

    return render(request, template)
