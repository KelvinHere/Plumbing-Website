from django.shortcuts import render
from .utils import set_session_vars_to_default


def home(request):
    set_session_vars_to_default(request)
    template = 'home/index.html'
    return render(request, template)


def contact(request):
    set_session_vars_to_default(request)
    template = 'home/contact.html'
    return render(request, template)


def delivery(request):
    set_session_vars_to_default(request)
    template = 'home/delivery.html'
    return render(request, template)


def about(request):
    set_session_vars_to_default(request)
    template = 'home/about.html'
    return render(request, template)


def specials(request):
    set_session_vars_to_default(request)
    template = 'home/specials.html'
    return render(request, template)