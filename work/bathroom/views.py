from django.shortcuts import render
from products.models import Category, Product


def bathroom(request):
    ''' Renders the bathroom information page '''
    request.session['shop_filter'] = 'bathroom'
    request.session['q'] = ''
    request.session['category'] = ''
    categories = Category.objects.values_list('name', flat=True)
    products_for_cards = []
    for category in categories:
        products_for_cards.append(Product.objects.filter(category__name=category).first())
    
    template = 'bathroom/bathrooms.html'

    context = {
        'products_for_cards': products_for_cards,
    }

    return render(request, template, context)