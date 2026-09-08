from django.db import models
from AccountApp.models import *
# Create your models here.
from store.models import Product,Variation

STATUS=(
    ('New','New'),
    ('Accepted','Accepted'),
    ('Completed','Completed'),
    ('Cancelled','Cancelled')
    )

class Payment(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    paymentId=models.CharField(max_length=100)
    paymentMethod=models.CharField(max_length=100)
    amountPaid=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.paymentId
class Order(models.Model):
    user=models.ForeignKey(Account,on_delete=models.SET_NULL,null=True)
    payment=models.ForeignKey(Payment,on_delete=models.SET_NULL,null=True)
    orderNumber=models.CharField(max_length=100)
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    phoneNumber=models.IntegerField()
    addressLine1=models.CharField(max_length=100)
    addressLine2=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    orderNote=models.TextField()
    orderTotal=models.FloatField()
    tax=models.FloatField()
    status=models.CharField(choices=STATUS,max_length=20)
    ip=models.URLField()
    is_order=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstName

    def fullName(self):
        return f"{self.firstName} {self.lastName}" 
    def fullAddress(self):
        
        return f"{self.addressLine1} {self.addressLine2}" 
class OrderProduct(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    variation=models.ForeignKey(Variation,on_delete=models.CASCADE)
    color=models.CharField(max_length=60)
    size=models.CharField(max_length=60)
    productPrice=models.FloatField()
    ordered=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.productName
    



