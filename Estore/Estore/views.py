from django.shortcuts import render
from store.models import *
def HomeView(request):
    products=Product.objects.all().filter(isAvailable=True)
    context={'products':products}
    return render(request,"home.html",context)