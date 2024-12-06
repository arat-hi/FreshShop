from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from Adminapp.models import ProductModel
from Userapp.models import Cart
# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(
            username = username,
            password=password,
            email=email
        )
        user.save()
        return redirect('/user')
    return render(request,'register.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('/user/home')
        else:
            return redirect('/register')

    return render(request,'login.html')

def view_product(request):
    product_obj = ProductModel.objects.all()
    if request.method == "POST":
        search = request.POST.get('q')
        if search:
            product_obj = ProductModel.objects.filter(product_name__icontains = search)
    return render(request, 'view_product.html', {'products': product_obj})





def AddCart(request, id):
    user = request.user
    product_obj = ProductModel.objects.get(product_id=id)
    try:
        cart_obj = Cart.objects.get(product=product_obj, user=user)
        quantity_change = request.GET.get('quantity', None)

        if quantity_change == 'decrease' and cart_obj.quantity > 1:
            cart_obj.quantity -= 1
        elif quantity_change == 'increase':
            cart_obj.quantity += 1

        cart_obj.save()

    except Cart.DoesNotExist:
        cart_obj = Cart(product=product_obj, user=user, quantity=1)
        cart_obj.save()

    return redirect('/user/home')


