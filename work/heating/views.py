from django.shortcuts import render


def heating(request):
    request.session['shop_filter'] = 'Heating'
    template = 'heating/heating.html'

    return render(request, template)


def heatingspares(request):
    request.session['shop_filter'] = 'Heating'
    template = 'heating/heatingspares.html'

    return render(request, template)


def heatpumps(request):
    request.session['shop_filter'] = 'Heating'
    request.session['category'] = ''
    template = 'heating/heatpumps.html'

    return render(request, template)


def renewables(request):
    request.session['shop_filter'] = 'Heating'
    request.session['category'] = ''
    template = 'heating/renewables.html'

    return render(request, template)


def stoves(request):
    request.session['shop_filter'] = 'Heating'
    request.session['category'] = ''
    template = 'heating/stoves.html'

    return render(request, template)