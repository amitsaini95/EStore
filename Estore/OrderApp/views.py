from django.shortcuts import render
from django.http import HttpResponse
from CartApp.models import CartItem
from .forms import *
# Create your views here.
def PlaceOrderView(request):
    currentUser=request.user
    cartItem=CartItem.objects.filter(user=currentUser)
    cartCount=cartItem.count()
    if cartCount <= 0:
        print("no")
    if request.method == "POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            data=Order()
            data.firstName=form.cleaned_data['firstName']
            data.lastName=form.cleaned_data['lastName']

            data.email=form.cleaned_data['email']
            data.phoneNumber=form.cleaned_data['phoneNumber']
            data.addressLine1=form.cleaned_data['addressLine1']
            data.addressLine2=form.cleaned_data['addressLine2']
            data.city=form.cleaned_data['city']
            data.state=form.cleaned_data['state']
            data.country=form.cleaned_data['country']
            data.orderNote=form.cleaned_data['orderNote']




    return HttpResponse("Place Order Here")