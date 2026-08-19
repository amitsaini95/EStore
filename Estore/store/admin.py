from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['productName','slug','price','category','productImage','isAvailable','stock']
admin.site.register(Product,ProductAdmin)