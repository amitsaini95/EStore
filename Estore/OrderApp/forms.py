from django.forms import ModelForm
from .models import *

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields=('firstName','lastName','email','phoneNumber','addressLine1','addressLine2','city','state','country','orderNote')