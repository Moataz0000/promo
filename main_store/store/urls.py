from django.urls import path
from . import views



app_name = 'store'


urlpatterns = [
    path('' , views.product_list , name='product_list'),
    path('products/' , views.store , name='products'),
    path('category/<slug:category_slug>/' , views.store , name='product_by_category'),
    path('<slug:category_slug>/' , views.product_list , name='product_list_by_category'),
    path('<int:id>/<slug:slug>/' , views.product_detail , name='product_detail'),
    path('<int:product_id>/comment/' , views.product_comment , name='product_comment')
    

]
