from django.urls import path
from .import views
urlpatterns = [
    path('registration-form',views.RegisterView,name="Register"),
    path('activate/<uidb64>/<token>/',views.ActivateView,name="activate"),
    path('login/',views.LoginView,name="Login"),
    path('dashboard',views.DashboardView,name="Dashboard"),
    path('logout',views.LogoutView,name="Logout")
]
