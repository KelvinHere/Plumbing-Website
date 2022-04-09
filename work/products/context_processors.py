from products.models import Category


def visitor_vars(request):
    ''' Context filter to preserve main query bar shop filter example heating or bathroom products '''
    shop_filter = request.session.get('shop_filter', 'All')
    categories = Category.objects.values_list('name', flat=True)

    query = request.session.get('q', None)

    context = {
        'shop_filter' : shop_filter,
        'q' : query,
        'categories' : categories,
    }

    return context