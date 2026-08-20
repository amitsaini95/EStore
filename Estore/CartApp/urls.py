from django.urls import path
from .import views
urlpatterns = [
    path('',views.CartView,name="Cartlist"),
    path('add-cart/<int:product_id>',views.AddCartView,name="addCart"),
    path('remove-cart/<int:product_id>',views.removeCartView,name="removeCart")
]
