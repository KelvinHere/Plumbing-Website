def set_session_vars_to_default(request):
    ''' Sets session context to default, ie no query / shop or category set '''
    request.session['shop_filter'] = 'all'
    request.session['q'] = ''
    request.session['category'] = ''
    return