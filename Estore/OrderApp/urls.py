from django.urls import path
from .import views
urlpatterns = [
    path('place-order/',views.PlaceOrderView,name="placeorder"),
    path('payments/',views.PaymentsView,name="payment")
]
