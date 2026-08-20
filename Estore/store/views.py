from django.shortcuts import render,get_object_or_404
from CategoryApp.models import Category
from .models import Product
# Create your views here.
def StoreView(request,slug=None):
    category=None
    products=None
    if slug!=None:
        category=get_object_or_404(Category,slug=slug)
        products=Product.objects.filter(category=category)
        
    else:
        products=Product.objects.filter(isAvailable=True)
        
    context={'products':products,'productCount':products.count()}
    return render(request,'store/store.html',context)

def ProductDetailCategoryView(request,category_slug,product_slug):
    try:
        singleproduct=Product.objects.get(category__slug=category_slug,slug=product_slug)

    except:
        pass
    context={'singleproduct':singleproduct}
    return render(request,"store/productDetails.html",context)
def CartView(request):
    return render(request,"store/cart.html")