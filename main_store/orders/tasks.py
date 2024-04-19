from celery import shared_task 
from django.core.mail import send_mail
from .models import Order
from io import BytesIO
import weasyprint # type: ignore
from django.template.loader import render_to_string
from django.core.mail import EmailMessage , send_mail
from orders.models import Order
from django.conf import settings
import os


# To Confirm Order
@shared_task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is successfully placed.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order Number. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order. Your order ID is {order.id}.\n' \
              f'Customer-Serves: 01001690789'
    mail_sent = send_mail(subject, message, 'motazfawzy73@gmail.com', [order.email])
    return mail_sent




# To Bill PDF 
@shared_task
def order_completed(order_id):
    try:
        order = Order.objects.get(id=order_id)
        subject = f'Promo - Invoice no. {order_id}'
        message = 'Please find attached the Invoice for your recent purchase.'
        
        # Generate PDF
        html = render_to_string('orders/pdf.html', {'order': order})
        out = BytesIO()
        css_path = os.path.join(settings.STATICFILES_DIRS[0], 'css', 'pdf.css')
        weasyprint.HTML(string=html).write_pdf(out, stylesheets=[weasyprint.CSS(css_path)])
        
        # Create email message
        email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [order.email])
        email.attach(f'order_{order_id}.pdf', out.getvalue(), 'application/pdf')
        
        # Send email
        email.send()
    except Order.DoesNotExist:
        raise ('Order Dose Not Exist!')
    except Exception as e:
        print(f"An error occurred: {str(e)}")



