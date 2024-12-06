from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Adminapp.models import ProductModel
from Userapp.models import Cart
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        user.save()
        return redirect('/user')
    return render(request, 'register.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/user/home')
        else:
            return redirect('/register')

    return render(request, 'login.html')


def view_product(request):
    product_obj = ProductModel.objects.all()
    if request.method == "POST":
        search = request.POST.get('q')
        if search:
            product_obj = ProductModel.objects.filter(product_name__icontains=search)
    return render(request, 'view_product.html', {'products': product_obj})


def logoutUser(request):
    logout(request)
    return redirect('/')


def AddCart(request, id):
    user = request.user
    product_obj = ProductModel.objects.get(product_id=id)
    try:
        cart_obj = Cart.objects.get(product=product_obj, user=user)
        quantity_change = request.GET.get('quantity', None)

        if quantity_change == 'decrease' and cart_obj.quantity > 1:
            cart_obj.quantity -= 1
        else:
            cart_obj.quantity += 1

        cart_obj.save()
        return redirect('/user/viewCart')
    except Cart.DoesNotExist:
        cart_obj = Cart(product=product_obj, user=user)
        cart_obj.save()
        return redirect('/user/viewCart')


def viewCart(request):
    user = request.user
    cart_obj = Cart.objects.filter(user=user)
    total_price = sum(item.total_price for item in cart_obj)
    delivery_tax = 2
    discount = 40
    coupon_discount = 10
    grand_total = total_price + delivery_tax - discount - coupon_discount
    if grand_total < 0:
        grand_total = 0
    else:
        grand_total = grand_total
    return render(request, 'cart.html',
                  {'data': cart_obj, 'total': total_price, 'delivery_tax': delivery_tax, 'discount': discount,
                   'coupon_discount': coupon_discount, 'grand_total': grand_total, })


def cartDelete(request, id):
    user = request.user
    cart_obj = Cart.objects.filter(cart_id=id, user=user)
    cart_obj.delete()
    return redirect('/user/home')


def checkOut(request):
    user = request.user
    cart_obj = Cart.objects.filter(user=user)
    total_price = sum(item.total_price for item in cart_obj)
    delivery_tax = 2
    discount = 40
    coupon_discount = 10
    grand_total = total_price + delivery_tax - discount - coupon_discount
    if grand_total < 0:
        grand_total = 0
    else:
        grand_total = grand_total

    return render(request, 'checkout.html', {'total': total_price, 'delivery_tax': delivery_tax, 'discount': discount,
                                             'coupon_discount': coupon_discount, 'grand_total': grand_total})


@login_required
def placeOrder(request):
    cart_obj = Cart.objects.filter(user=request.user)
    cart_obj.delete()
    messages.success(request, "Item ordered successfully")
    return redirect('/user/home')
