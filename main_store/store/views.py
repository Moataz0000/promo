from django.shortcuts import render , get_object_or_404
from .models import Category , Product
from cart.forms import CartAddProductForm
from django.views.decorators.http import require_POST
from .forms import CommentForm


def product_list(request , category_slug=None):
    MAX_PRODUCTS = 8
    category = None
    categories = Category.objects.all()
    products = Product.objects.all().filter(available=True , status=Product.Status.Regularproduct).order_by('-created')[:MAX_PRODUCTS]
    ProductOffers = Product.objects.all().filter(available=True , status=Product.Status.ProductOffers).order_by('-created')[:MAX_PRODUCTS]
    if category_slug:
        category = get_object_or_404(Category , slug=category_slug)
        products = products.filter(category=category)
    context = {
        'categories':categories,
        'category':category,
        'products':products,
        'productoffers':ProductOffers,
    }    
    return render(request , 'store/home.html' , context)





def product_detail(request , id , slug):
    product = get_object_or_404(Product , id=id , slug=slug , available=True)
    cart_product_form = CartAddProductForm()
    comments = product.comments.filter(active=True)
    form = CommentForm()
    context = {
        'product':product,
        'cart_product_form':cart_product_form,
        'comments':comments,
        'form':form,
        
    }
    return render(request , 'store/product_detail.html' , context)





def store(request , category_slug=None) -> None:
    category = None
    categories = Category.objects.all()
    products = Product.objects.all().filter(available=True).order_by('-created')
    if category_slug:
        category = get_object_or_404(Category , slug=category_slug)
        products = products.filter(category=category)
    # hendle search  
    name = None
    price_form = None
    price_to = None
    if 'query' in request.GET:
        name = request.GET['query'] 
        if name: # check name is exsist ?
            products = products.filter(name__icontains=name) 
    
    if 'searchpricefrom' in request.GET and 'searchpriceto' in request.GET:
        price_form = request.GET['searchpricefrom']
        price_to = request.GET['searchpriceto']
        if price_form and price_to:  # check price is exsist ?
            if price_form.isdigit() and price_to.isdigit(): # check price is digit !
                products = products.filter(price__gte=price_form , price__lte=price_to)

   
    context = {
        'categories':categories,
        'category':category,
        'products':products,
    }

    return render(request, 'store/store.html' , context)

"""
We use the require_POST decorator provided by Django to
only allow POST requests for this view 
"""


@require_POST
def product_comment(request , product_id):
    prodcut = get_object_or_404(Product , id=product_id , available=True)
    comment = None

    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.prodcut = prodcut
        comment.save()
    context = {
        'form':form,
        'comment':comment, 
        'product':prodcut,
    }    

    return render(request , 'sotre/comment.html' , context)

