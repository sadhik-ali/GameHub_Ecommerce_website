from django.contrib import admin
from django.urls import path, include
from .import views
from . views import index, detail_page


urlpatterns = [
    path('',index.as_view(),name="index"),
    path('detail_page/<int:pk>',detail_page.as_view(),name="detail_page"),
    path('cart_detail',views.cart_detail,name='cart_detail'),
    path('checkout',views.checkout,name='checkout'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('success',views.success,name='success'),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),



]

