from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="user_home"),
    path('user_store/', views.store, name="user_store"),
    path('user_cart/', views.cart, name="user_cart"),
    path('user_checkout/', views.checkout, name="user_checkout"),
]