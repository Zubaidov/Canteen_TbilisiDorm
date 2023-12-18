from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from .models import Menu


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
    myproducts = Menu.published.all()
    context={
        "myproducts" : myproducts,
    }
    return render(request, 'menu.html', context)

def productSingle(request, year, month, day, slug):
    
    myproducts = get_list_or_404(Menu, status=Menu.Status.PUBLISHED, 
                                 publish__year = year, 
                                 publish__month = month, 
                                 publish__day = day, 
                                 slug = slug)
    context = {
        "myproducts": myproducts,
    }
    return render(request, 'product-single.html', context)


def blogs(request):
    context={}
    return render(request, 'blogs.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def error404(request):
    context={}
    return render(request, 'error404.html', context)
