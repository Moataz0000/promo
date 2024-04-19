from django.shortcuts import render , get_object_or_404
from .models import OrderItem , Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created , order_completed
from django.contrib.admin.views.decorators import staff_member_required


# bill pdf
import weasyprint # type: ignore
from django.template.loader import render_to_string
from django.conf import settings
from django.http import HttpResponse





def order_create(request):
    cart = Cart(request)  # get cart from the session
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])

            cart.clear()
            order_created.delay(order.id)  # excute the task
            order_completed.delay(order.id)  # excute the task

            return render(request, 'orders/created.html', {'order': order})  # Corrected the context dictionary
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})

from django.shortcuts import render
from django.http import HttpResponse
from .tasks import order_completed





def user_orders(request):
    orders = OrderItem.objects.all()
    order_id = request.GET.get('trakingorder')

    if order_id and order_id.isdigit():
        # Use filter to get orders with the specified ID
        orders = orders.filter(id=int(order_id))

    context = {
        'orders': orders,
    }

    return render(request, 'orders/tracking_order.html', context)
from cart.cart import Cart
import os

@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/pdf.html', {'order': order })
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order_id}.pdf'
    css_path = os.path.join(settings.STATICFILES_DIRS[0], 'css', 'pdf.css')
    weasyprint.HTML(string=html).write_pdf(response, stylesheet=[weasyprint.CSS(css_path)])
    return response
