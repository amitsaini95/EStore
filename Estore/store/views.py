from django.shortcuts import render,get_object_or_404
from CategoryApp.models import Category
from .models import Product
from django.db.models import Q
from CartApp.models import *
from CartApp.views import _cart_id
from django.core.paginator import Paginator
# Create your views here.
def StoreView(request,slug=None):
    category=None
    products=None

    if slug!=None:
        category=get_object_or_404(Category,slug=slug)
        products=Product.objects.filter(category=category)
        paginator=Paginator(products,6)
        page=request.GET.get('page')
        paged_paginator=paginator.get_page(page)
        last_page=paged_paginator.paginator.num_pages
    else:
        products=Product.objects.filter(isAvailable=True)
        paginator=Paginator(products,4)
        page=request.GET.get('page')
        paged_paginator=paginator.get_page(page)
        last_page=paged_paginator.paginator.num_pages
        

        
    context={'products':paged_paginator,'numberofpage':[n+1 for n in range(last_page)],'last_page':last_page,'productCount':products.count()}
    return render(request,'store/store.html',context)

def ProductDetailCategoryView(request,category_slug,product_slug):
    
    try:
        singleproduct=Product.objects.get(category__slug=category_slug,slug=product_slug)
        inCartitems=CartItem.objects.filter(cart__cartId=_cart_id(request),product=singleproduct).exists()
        

    except:
        pass
    context={'singleproduct':singleproduct,'incartitems':inCartitems}
    return render(request,"store/productDetails.html",context)


def SearchView(request):
    products=''
    productCount=0
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword :
            products=Product.objects.order_by('-created').filter(Q(productName__icontains=keyword) | Q(category__categoryName__icontains=keyword))
            productCount=products.count()
    context={
        'products':products,
        'productCount':productCount
    }
    return render(request,"store/store.html",context)