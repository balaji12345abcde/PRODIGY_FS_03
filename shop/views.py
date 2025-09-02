from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order
from .forms import ProductForm, ReviewForm, SupportForm
import json

def home(request):
    qs = Product.objects.all().order_by('-created_at')
    q = request.GET.get('q')
    category = request.GET.get('category')
    sort = request.GET.get('sort')
    if q:
        qs = qs.filter(name__icontains=q)
    if category:
        qs = qs.filter(category__iexact=category)
    if sort == 'price_asc':
        qs = qs.order_by('price')
    if sort == 'price_desc':
        qs = qs.order_by('-price')
    return render(request, 'shop/home.html', {'products':qs})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ReviewForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        review = form.save(commit=False)
        review.product = product
        review.save()
        return redirect('product_detail', pk=pk)
    return render(request, 'shop/product_detail.html', {'product':product, 'form':form})

# Simple session-cart: {'product_id': quantity}
def add_to_cart(request, pk):
    cart = request.session.get('cart', {})
    cart[str(pk)] = cart.get(str(pk), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')

def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for pid, qty in cart.items():
        try:
            p = Product.objects.get(pk=int(pid))
            subtotal = p.price * qty
            items.append({'product':p,'qty':qty,'subtotal':subtotal})
            total += subtotal
        except Product.DoesNotExist:
            continue
    return render(request, 'shop/cart.html', {'items':items,'total':total})

def update_cart(request):
    if request.method == 'POST':
        cart = {}
        for key, val in request.POST.items():
            if key.startswith('qty_'):
                pid = key.split('_',1)[1]
                try:
                    q = int(val)
                    if q > 0:
                        cart[pid] = q
                except: pass
        request.session['cart'] = cart
    return redirect('cart')

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('home')
    items = []
    total = 0
    for pid, qty in cart.items():
        p = Product.objects.get(pk=int(pid))
        items.append({'name':p.name,'qty':qty,'price':float(p.price)})
        total += float(p.price) * qty
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        o = Order.objects.create(name=name,email=email,address=address,items=json.dumps(items),total=total)
        request.session['cart'] = {}
        return render(request, 'shop/order_success.html', {'order':o})
    return render(request, 'shop/checkout.html', {'items':items,'total':total})

def orders(request):
    qs = Order.objects.all().order_by('-created_at')
    return render(request, 'shop/orders.html', {'orders':qs})

def add_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'shop/add_product.html', {'form':form})

def support(request):
    form = SupportForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'shop/support.html', {'form':form})
