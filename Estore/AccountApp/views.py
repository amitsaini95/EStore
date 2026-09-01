from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm
# Create your views here.
from django.contrib import messages
from django.contrib.auth import *
from .models import Account
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
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
            currentSite=get_current_site(request)
            mail_subject='please activate your Account'
            message=render_to_string("acccountVerificationEmail.html",{'user':user,'domain':currentSite,'uid':urlsafe_base64_encode(force_bytes(user.pk)),'token':default_token_generator.make_token(user)})
            print(message)
            to_email=email
            send_email=EmailMessage(mail_subject,message,to=[to_email])
            
            send_email.send()
            
            return redirect('login/?command=verification&email='+email)

    else:
        form=RegistrationForm()
    context={
        'form':form
    }
    return render(request,"registration.html",context)
def LoginView(request):
    if request.method == "POST":
        form=LoginForm(data=request.POST,request=request)
        if form.is_valid():
            email = form.cleaned_data['email'] 
            password = form.cleaned_data['password']
            user = authenticate(email=email,password=password)
            if user is  not None: 
                login(request,user)
              
                messages.success(request,"logged in successfully ||")
                return redirect('Home')
            else:
               
                messages.error(request,"invalid login credentials")
    else:
        form=LoginForm()

    context={
        'form':form
    }
    return render(request,"login.html",context)

def ActivateView(request,uidb64,token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=Account._default_manager.get(pk=uid)
    except(TypeError,OverflowError,ValueError,Account.DoesNotExist):
        user=None
    if user is not None and default_token_generator.make_token(user):
        user.is_active=True
        user.save()
        messages.success(request,"congratulations Your Account is  Activated")
        return redirect('Login')
    else:
        messages.error(request,"invalid activate Link")
        return redirect('Home')