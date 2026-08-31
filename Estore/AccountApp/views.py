from django.shortcuts import render,redirect
from .forms import RegistrationForm
# Create your views here.
from django.contrib import messages
from .models import Account
def RegisterView(request):
    if request.method == "POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            phoneNumber=form.cleaned_data['phoneNumber']
            password=form.cleaned_data['password']
            user=Account.objects.create(username=username,email=email,phoneNumber=phoneNumber)
            user.set_password(password)
            user.save()
            messages.success(request,"registration successful")
           
            

    else:
        form=RegistrationForm()
    context={
        'form':form
    }
    return render(request,"registration.html",context)