from django.urls import path
from .import views
urlpatterns = [
    path('',views.StoreView,name="storeList"),
    path('<slug:slug>/',views.StoreView,name="CategoryProduct"),
    path('<slug:category_slug>/<slug:product_slug>/',views.ProductDetailCategoryView,name="productdetailCat"),
    path('search',views.SearchView,name="Search")
]
