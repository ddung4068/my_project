from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.sign_in,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.sign_out,name='logout'),
    path('analyst/',views.analyst,name='analyst'),
]