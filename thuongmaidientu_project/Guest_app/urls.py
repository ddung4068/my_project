# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # list phone
    path('list_iphone/', views.list_iphone , name= 'list_iphone'),
    path('list_samsung/', views.list_samsung , name= 'list_samsung'),
    path('list_xiaomi/', views.list_xiaomi , name= 'list_xiaomi'),
    # list laptop
    path('list_macbook/', views.list_macbook , name= 'list_macbook'),
    path('list_lenovo/', views.list_lenovo , name= 'list_lenovo'),
    path('list_dell/', views.list_dell , name= 'list_dell'),
    # list apple watch
    path('list_apple_watch/', views.list_apple_watch , name= 'list_apple_watch'),
    path('list_samsung_watch/', views.list_samsung_watch , name= 'list_samsung_watch'),
    path('list_xiaomi_watch/', views.list_xiaomi_watch , name= 'list_xiaomi_watch'),
    # list apple watch
    path('list_airpods/', views.list_airpods , name= 'list_airpods'),
    path('list_samsung_headphone/', views.list_samsung_headphone , name= 'list_samsung_headphone'),
    path('list_xiaomi_headphone/', views.list_xiaomi_headphone , name= 'list_xiaomi_headphone'),
    # list Tivi
    path('list_samsungTV/', views.list_samsungTV , name= 'list_samsungTV'),
    path('list_xiaomiTV/', views.list_xiaomiTV , name= 'list_xiaomiTV'),
    

    # chi tiết sản phẩm
    path('detail_phone/<int:id>/', views.detail_phone, name='detail_phone'),
    path('detail_laptop/<int:id>/', views.detail_laptop, name='detail_laptop'),
    path('detail_smartwatch/<int:id>/', views.detail_smartwatch, name='detail_smartwatch'),
    path('detail_headphone/<int:id>/', views.detail_headphone, name='detail_headphone'),
    path('detail_TV/<int:id>/', views.detail_TV, name='detail_TV'),
    
    # giỏ hàng
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    # chỉnh sửa số lượng
    path('edit_product/<int:id>/', views.edit_product, name='edit_product'),
    # xóa khỏi giỏ hàng
    path('remove_product/<int:id>/', views.remove_product, name='remove_product'),
    # đặt hàng
    path('check_out/', views.check_out, name='check_out'),
    # thông tin đơn hàng sau khi đặt
    path('checkout_detail/<int:id>/', views.checkout_detail, name='checkout_detail'),
]