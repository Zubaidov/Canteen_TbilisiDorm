from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    context = {}
    return render(request, 'index.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def reservation(request):
    context = {}
    return render(request, 'reservation.html', context)

def menu(request):
    context={}
    return render(request, 'menu.html', context)

def blogs(request):
    context={}
    return render(request, 'blogs.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def error404(request):
    context={}
    return render(request, 'error404', context)