# urls.py

from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


app_name = 'seller_account'

urlpatterns = [

    path('' , include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    # path('edit/', views.edit, name='edit'),


]
