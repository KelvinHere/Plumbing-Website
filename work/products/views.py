from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.postgres import search
from django.contrib.postgres.search import SearchVector, SearchRank
import re

from .models import Product

def products(request):

    # Initialise page
    shop_filter = 'All'
    shop_filter_list = ['All', 'Bathroom', 'Heating', 'Plumbing']
    category = request.session.get('category', '')

    # GET: setup shop_filter & categories
    if request.GET:
        if 'shop_filter' in request.GET:
            shop_filter = request.GET.get('shop_filter')
            request.session['shop_filter'] = shop_filter
        if 'category' in request.GET:
            category = request.GET.get('category')
            request.session['category'] = category

    # POST: retrieve and set shop/category filters
    if request.method == 'POST':
        # Get and set shop
        if request.POST.get('shop-filter') in shop_filter_list: # If shop is valid
            shop_filter = request.POST.get('shop-filter')       # Set shop
            request.session['shop_filter'] = shop_filter        # Store selection in sessions
        # Get and set Query
        if request.POST.get('q'):
            query = request.POST.get('q')
            query = re.sub(r'[!\'()|&]', ' ', query).strip()
            request.session['q'] = query
        else:
            query = None
            request.session['q'] = query

    # Get products
    products = Product.objects.all()

    # Filter by shop
    if shop_filter != 'All':
        products = products.filter(shop__name=shop_filter)

    # Rank results by user query
    if request.session.get('q'):
        query = request.session.get('q')
        # Grab numbers matching the format 800x1000
        measurements = re.compile(r'(\d{3,})\s(\d{3,})')
        matches = measurements.findall(query)
        # Add postgres partial word search
        query = re.sub(r'\s+', ':* & ', query)
        query += ':*'
        searchQuery = search.SearchQuery(query, search_type='raw')
        vector = SearchVector('sku', weight='A') + SearchVector('name', weight='B') + SearchVector('description', weight='C')
        products = products.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.1).order_by('-rank')
    else:
        products = products.order_by('id')

    template = 'products/products.html'
    context = {
        'products': products,
        'category': category,
    }

    return render(request, template, context)