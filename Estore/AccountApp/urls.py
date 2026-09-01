from django.urls import path
from .import views
urlpatterns = [
    path('',views.RegisterView,name="Register"),
    path('activate/<uidb64>/<token>/',views.ActivateView,name="activate"),
    path('login/',views.LoginView,name="Login")
]
