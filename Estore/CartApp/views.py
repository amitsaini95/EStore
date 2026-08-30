from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import *
from .models import *
# Create your views here.

from django.db.models import Q
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart
def AddCartView(request,product_id):
    productVariation=[]
    variationId=[]
    cartId=[]
    product=Product.objects.get(id=product_id)
    if request.method =="POST":
        addCartItemID=request.POST.get('cartItemAddCart')
        cartId = addCartItemID
        for item in request.POST:
            key=item
            value=request.POST[key]
       
            try:
                variations=Variation.objects.get(product=product,variationCategory__iexact=key,variationValue__iexact=value)
                productVariation.append(variations)

            except:
                pass

    try:
        cart=Cart.objects.get(cartId=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cartId=_cart_id(request))
    cart.save()
    cartitemExist=CartItem.objects.filter(product=product,cart=cart)
    if cartitemExist.exists():
        cartItemAdd=CartItem.objects.filter(product=product,cart=cart)
        cartIDAdd=[]
        for item in cartItemAdd:
            variationId.append(list(item.variation.all()))
            cartIDAdd.append(item.id)
        if productVariation in variationId:
            index=variationId.index(productVariation)
            item_id=cartIDAdd[index]
            cart=CartItem.objects.get(id=item_id,product=product)
            cart.quantity+=1
            cart.save()
          
        else:
            cartitemNEw=CartItem.objects.create(product=product,cart=cart,quantity=1)
            if len(productVariation)>0:
                cartitemNEw.variation.clear()
                cartitemNEw.variation.add(*productVariation)
            cartitemNEw.save()
    
    else:
        cartItemNew=CartItem.objects.create(product=product,cart=cart,quantity=1)
        if len(productVariation)>0:
            cartItemNew.variation.clear()
            cartItemNew.variation.add(*productVariation)
        cartItemNew.save()
    return redirect('Cartlist')


def QuantityAddCartItemView(request,cart_id):
    cartitem=CartItem.objects.get(id=cart_id)
    cartitem.quantity+=1
    cartitem.save()

    return redirect("Cartlist")
def QuantitySubCartItemView(request,cart_id):
    cartitem=CartItem.objects.get(id=cart_id)
    if cartitem.quantity>1:
        cartitem.quantity-=1
        cartitem.save()
       
    return redirect('Cartlist')

def removeCartButtonView(request,product_id):
    getcartitem=CartItem.objects.get(id=product_id)
    getcartitem.delete()
    return redirect('Cartlist')
def CartView(request,total=0,quantity=0,getcartitem=None):
    try:
        tax=0
        grandTotal=0
        cart=Cart.objects.get(cartId=_cart_id(request))
        getcartitem=CartItem.objects.filter(cart=cart,isActive=True)
        for cartproduct in getcartitem:
            total+=(cartproduct.product.price * cartproduct.quantity)
            quantity+=cartproduct.quantity
        tax=(2*total)/100
        grandTotal=total+tax
    
    except:
        pass
    context={
        'cartitems':getcartitem,
        'quantity':quantity,
        'total':total,
        'tax':tax,
        'grandTotal':grandTotal 
    }
    return render(request,"store/cart.html",context)