from django.contrib import admin
from django.urls import path, include
from .import views
from . views import index, Detail_Page


urlpatterns = [
    path('',index.as_view(),name="index"),
    path('Detail_page/<int:pk>',Detail_Page.as_view(),name="Detail_Page"),
    path('cart_detail',views.cart_detail,name='cart_detail'),
    path('checkout',views.checkout,name='checkout'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('success',views.success,name='success'),
]

