from django.urls import path
from . import views


app_name = 'seller'


urlpatterns = [
    path('why-us/' , views.why_us , name='why_us'),
    path('download-pdf/', views.download_pdf, name='download_pdf'),
    path('dashboard' , views.dashboard , name='dashboard'),
    path('my-products/' , views.products , name='products'),
    path('successfully/' , views.successfully , name='successfully'),
    path('analytics/' , views.analytics , name='analytics'),
    path('<int:id>/update-product/' , views.update , name='update'),
    path('delete/<int:id>/' , views.delete , name='delete'),
    path('order/<int:id>/delete/', views.order_delete, name='order_delete'),





    

]

