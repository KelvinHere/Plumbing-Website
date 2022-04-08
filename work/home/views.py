from django.shortcuts import render, HttpResponse
from products.models import Product
import json

def home(request):
    data = Product.objects.all()
    template = "home/index.html"
    context = {
        'data': data,
    }
    return render(request, template, context)
