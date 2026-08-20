from django.db import models
from store.models import *
# Create your models here.
class Cart(models.Model):
    cartId=models.CharField(max_length=100)
    dateAdded=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cartId
class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="CartProducts")
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    isActive=models.BooleanField(default=True)


    def sub_total(self):
        return self.product.price * self.quantity
    def __str__(self):
        return self.product.productName

