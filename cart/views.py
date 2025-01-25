from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core.mail import send_mail
from main.models import Product
from commerce import settings


# Create your views here.

@csrf_exempt
def cart_(request):
    # get the cart
    cart = Cart(request)
    cart_products = cart.get_products()
    quantities = cart.get_quants()
    totals = cart.cart_total()
    return render(request, '_update/cart.html',
                  {'products': cart_products, 'quantities': quantities, 'totals': totals})

def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_products()
    quantities = cart.get_quants()
    totals = cart.cart_total()
    return render(request, '_update/checkout.html',{'products': cart_products, 'quantities': quantities, 'totals': totals})

@csrf_exempt
def add_item(request):
    cart = Cart(request)
    # post test
    if request.POST.get('action') == 'post':
        # get the data
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        # look data
        print(product_id, product_qty)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        # cart quantity
        cart_qnt = cart.__len__()
        # response return
        messages.success(request, f'Added Successfully')
        response = JsonResponse({'Product Id': product_id, 'Product Qty': product_qty, 'qty': cart_qnt})

        return response

@csrf_exempt
def delete_item(request):
    cart = Cart(request)
    # post test
    if request.POST.get('action') == 'post':
        # get the data
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response = JsonResponse({'Product Deleted ID': product_id})
        messages.error(request, f'Product deleted from cart')
        return response


@csrf_exempt
def update_item(request):
    cart = Cart(request)
    # post test
    if request.POST.get('action') == 'post':
        # get the data
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({'Product ID': product_id, 'qty': product_qty})
        return response


@csrf_exempt
def payment(request):
    pass
