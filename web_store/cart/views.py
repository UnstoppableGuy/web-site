from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from first_app.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponApplyForm


@require_POST
def cart_add(request, product_id):
    '''
    Вызывается из продукта, откуда и берется product_id.
    '''
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                quantity=cd['quantity'],
                update_quantity=cd['update_quantity'])

    return redirect('cart:cart_detail')

def cart_remove(request, product_id): # pragma: no cover
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)

    return redirect('cart:cart_detail')

'''
Также обрабатывает купон.
'''
def cart_detail(request): 
    cart = Cart(request)

    coupon_apply_form = CouponApplyForm()
    context = {'cart': cart, 'coupon_apply_form': coupon_apply_form}

    return render(request, 'cart/detail.html', context)
