from django.shortcuts import render,redirect
from django.http import HttpResponse
from CartApp.models import CartItem
from .forms import *
import datetime
# Create your views here.
def PlaceOrderView(request):
    currentUser=request.user
    cartItem=CartItem.objects.filter(user=currentUser)
    cartCount=cartItem.count()
    if cartCount <= 0:
        return redirect('Cartlist')
    tax=0
    total=0
    grandTotal=0
    for cart in cartItem:
        total+=(cart.product.price * cart.quantity)
        print(total)

    tax=(2*total)/100
    grandTotal=total+tax
    

    if request.method == "POST":
        
            data=Order()
            data.firstName=request.POST.get('firstName')
            data.lastName=request.POST.get('lastName')
            data.email=request.POST.get('email')
            data.phoneNumber=request.POST.get('phoneNumber')
            data.addressLine1=request.POST.get('addressLine1')
            data.addressLine2=request.POST.get('addressLine2')
            data.city=request.POST.get('city')
            data.state=request.POST.get('state')
            data.orderNote=request.POST.get('orderNote')
            data.orderTotal=grandTotal
            data.tax=tax
            data.ip=request.META.get('REMOTE_ADDR')
            year=int(datetime.date.today().strftime('%y'))
            month=int(datetime.date.today().strftime('%m'))
            dt=int(datetime.date.today().strftime('%d'))
            d=datetime.date(year,month,dt)
            currentDate=d.strftime("%Y%m%d")
            orderNumber=currentDate+str(data.id)
            data.orderNumber=orderNumber
            data.save()
            return redirect('Home')
    
