from django.contrib import admin
from .models import *
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display=['product','quantity','isActive','color','size']
    def color(self,obj):
        return [i for i in obj.variation.colors()]
    def size(self,obj):
            return [i for i in obj.variation.sizes()]
admin.site.register(Cart)

admin.site.register(CartItem,CartAdmin)