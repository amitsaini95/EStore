from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['productName','slug','price','category','productImage','isAvailable','stock']

class VariationAdmin(admin.ModelAdmin):
    list_display=['product','variationCategory','variationValue','isActive']
admin.site.register(Product,ProductAdmin)
admin.site.register(Variation,VariationAdmin) 