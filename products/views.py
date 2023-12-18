from django.shortcuts import render
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
    myproducts = Menu.objects.all()
    context={
        "myproducts" : myproducts,
    }
    return render(request, 'menu.html', context)

def blogs(request):
    context={}
    return render(request, 'blogs.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def error404(request):
    context={}
    return render(request, 'error404.html', context)

def productSingle(request, id):
    myproducts = Menu.objects.all().get(id=id)
    context = {
        "myproducts": myproducts,
    }
    return render(request, 'productSingle.html', context)