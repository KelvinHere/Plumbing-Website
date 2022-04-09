from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.postgres import search
from django.core.paginator import Paginator, EmptyPage
from django.contrib.postgres.search import SearchVector, SearchRank
from .models import Product, Shop
import re
from django.template import RequestContext


def products(request):

    # Initialise page
    page_number = 1
    products_per_page = 40
    shop_filter = 'all'
    shop_filter_list = list(Shop.objects.values_list('name', flat=True))
    category = request.session.get('category', '')

    # GET: setup shop_filter & categories
    if request.GET:
        print('in get')
        if 'page' in request.GET:
            page_number = request.GET.get('page')
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
            shop_filter = request.POST.get('shop-filter')       
            request.session['shop_filter'] = shop_filter
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
    if shop_filter != 'all':
        products = products.filter(shop__name=shop_filter)

    if category:
        products = products.filter(category__name=category)

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

    # Pagination
    p = Paginator(products, products_per_page)
    page_object = p.get_page(page_number)

    try:
        page_object = p.page(page_number)
    except EmptyPage:
        page_object = p.page(1)
    
    template = 'products/products.html'
    context = {
        'products': page_object,
        'category': category,
    }

    return render(request, template, context)