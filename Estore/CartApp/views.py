from django.shortcuts import render,redirect
from store.models import *
from .models import *
# Create your views here.
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart
def AddCartView(request,product_id):
    product=Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cartId=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cartId=_cart_id(request))
    cart.save()
    try:
        cart_item=CartItem.objects.get(product=product,cart=cart)
        cart_item.quantity+=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(product=product,cart=cart,quantity=1)
    
        cart_item.save()
    return redirect('Cartlist')

def removeCartView(request,product_id):
    cart=Cart.objects.get(cartId=_cart_id(request))
    product=Product.objects.get(id=product_id)
    cart_items=CartItem.objects.get(product=product,cart=cart)

    if cart_items.quantity>1:
        cart_items.quantity-=1
        cart_items.save()
    else:
        cart_items.quantity=1
        cart_items.save()
    return redirect('Cartlist')
    

def removeCartButtonView(request,product_id):
    cart=Cart.objects.get(cartId=_cart_id(request))
    product=Product.objects.get(id=product_id)
    cart_items=CartItem.objects.get(product=product,cart=cart)
    cart_items.delete()
    return redirect('Cartlist')
def CartView(request,total=0,quantity=0,cart_items=None):
    try:
        cart=Cart.objects.get(cartId=_cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart,isActive=True)
        for cartproduct in cart_items:
            total+=(cartproduct.product.price * cartproduct.quantity)
            quantity+=cartproduct.quantity
        tax=(2*total)/100
        grandTotal=total+tax
    
    except:
        pass
    context={
        'cartitems':cart_items,
        'quantity':quantity,
        'total':total,
        'tax':tax,
        'grandTotal':grandTotal 
    }
    return render(request,"store/cart.html",context)