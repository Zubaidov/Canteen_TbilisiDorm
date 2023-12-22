from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from .models import Products, Chefs, PageAbout, Category
from django.core.mail import send_mail

def index(request):
    chefs = Chefs.objects.all()
    context = {'chefs': chefs}
    return render(request, 'index.html', context)

def about(request):
    aboutstory = PageAbout.objects.all()
    context = {
        'aboutstory':aboutstory
        }
    return render(request, 'about.html', context)

def products(request):
    myproducts = Products.published.all()
    context={
        "myproducts" : myproducts,
    }
    return render(request, 'products.html', context)

def product(request, year, month, day, slug):
    
    myproducts = get_list_or_404(Products, status=Products.Status.PUBLISHED, 
                                 publish__year = year, 
                                 publish__month = month, 
                                 publish__day = day, 
                                 slug = slug)
    context = {
        "myproducts": myproducts,
    }
    return render(request, 'product.html', context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def error404(request):
    context={}
    return render(request, 'error404.html', context)
