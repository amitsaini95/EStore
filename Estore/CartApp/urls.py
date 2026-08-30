from django.urls import path
from .import views
urlpatterns = [
    path('',views.CartView,name="Cartlist"),
    path('add-cart/<int:product_id>',views.AddCartView,name="addCart"),
    path('cart-item-add/<int:cart_id>',views.QuantityAddCartItemView,name="quanatiyAddCartItem"),
    path('cart-item-sub/<int:cart_id>',views.QuantitySubCartItemView,name="quantitysubCartItem"),
    path('remove-cart-item/<int:product_id>',views.removeCartButtonView,name="removeCartButton")
]
