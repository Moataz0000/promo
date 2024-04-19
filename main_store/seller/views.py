from django.shortcuts import render , redirect , get_object_or_404
from django.http import FileResponse
from django.conf import settings
import os
from .forms import ProductForm , OrderForm
from store.models import Product
from orders.models import OrderItem , Order
from django.contrib.auth.decorators import login_required



def why_us(request):
    return render(request , 'seller/why_us.html')




def download_pdf(request):
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'pdf/beginer.pdf')
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')



def dashboard(request , ):
    orders = OrderItem.objects.all().order_by('-created')
    context = {
        'orders':orders
    }

    return render(request , 'seller/dashboard_sell.html' , context)




@login_required
def products(request):
    seller_id = request.user.id  # Assuming seller_id is the same as user id
    if request.method == 'POST':
        add_product = ProductForm(request.POST, request.FILES)
        if add_product.is_valid():
            # Set the seller for the product before saving
            product = add_product.save(commit=False)
            product.seller_id = seller_id
            product.save()
            return redirect('seller:successfully')

    forms = ProductForm()
    # Filter products based on the seller_id
    seller_products = Product.objects.filter(seller_id=seller_id).order_by('-created')
    context = {
        'form': forms,
        'seller_products': seller_products,
    }
    return render(request, 'seller/products_seller.html', context)


def successfully(request):
    return render(request , 'seller/success.html')



@login_required
def update(request , id):
    product_id = Product.objects.get(id=id , available=True)
    if request.method == 'POST':
        product_save = ProductForm(request.POST , request.FILES , instance=product_id)
        if product_save.is_valid():
            product_save.save()
            return redirect('seller:products')
    else:
        product_save = ProductForm(instance=product_id) 
    context = {
        'form':product_save
    }           


    return render(request , 'seller/update.html' , context)


@login_required
def delete(requset , id):
    product_delete = get_object_or_404(Product , id=id , available=True)
    if requset.method == 'POST':
        product_delete.delete()
        return redirect('seller:products')
    return render(requset , 'seller/delete.html')






@login_required
def order_delete(request, id):
    # Get the order or return a 404 error if it doesn't exist
    order = get_object_or_404(OrderItem, id=id)
    
    if request.method == 'POST':
        order.delete()
        return redirect('seller:dashboard')
    context = {
        'order_id':order
    }

    return render(request, 'seller/order_delete.html' , context)



def status(request):
    orders = OrderItem.objects.all()
    
    rejections = orders.filter(status=OrderItem.Status.Rejection)
    shippings = orders.filter(status=OrderItem.Status.Shipping)
    processings = orders.filter(status=OrderItem.Status.Pending)
    
    context = {
        'orders': orders.count(),
        'rejections_count': rejections.count(),
        'shipping_count': shippings.count(),
        'processing_count': processings.count(),
        
    }

    return render(request, 'n_f_dash/status.html', context)



def analytics(request):
    return render(request , 'seller/analytics.html')



