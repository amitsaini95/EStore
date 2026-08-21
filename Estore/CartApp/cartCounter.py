from .views import _cart_id
from .models import CartItem,Cart

def cartCounterItem(request):


    counter=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cartId=_cart_id(request))
            cartitems=CartItem.objects.all().filter(cart=cart[:1])
            for item in cartitems:
                counter+=item.quantity


        except Cart.DoesNotExist:
            counter=0
            pass
    return dict(counter=counter)