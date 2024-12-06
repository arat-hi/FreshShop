from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')


def add(request):
    if request.method == "POST":
        product_obj = ProductModel()
        product_obj.product_name = request.POST['name']
        product_obj.description = request.POST['description']
        product_obj.price = request.POST['price']
        product_obj.image = request.FILES['image']
        product_obj.save()
        return redirect('/')
    return render(request, 'add.html')



