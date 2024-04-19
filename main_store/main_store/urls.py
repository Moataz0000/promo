from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

admin.site.index_title = "Promo"
admin.site.site_header = "Promo Admin"
admin.site.site_title = "Promo-Ecommerce"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/' , include('accounts.urls' , namespace='accounts')),
    path('contact-us/' , include('contactus.urls' , namespace='contactus')),
    path('cart/' , include('cart.urls' , namespace='cart')),
    path('coupons/', include('coupons.urls', namespace='coupons')),
    path('orders/' , include('orders.urls' , namespace='orders')),
    path('' , include('store.urls', namespace='store')),
    path('join-US-seller/' , include('seller.urls' , namespace='seller')),
    path('seller/account/' , include('seller_account.urls' , namespace='seller_account')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
