from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail






def contact_us(request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # name = f"From :{cd['name']}"
            subject = f"{cd['subject']}"
            message = f"{cd['message']}"
            send_mail(subject , message , 'motazfawzy73@gmail.com' , [cd['email']])
            sent = True
    else:
        form = ContactForm()    

    return render(request , 'contactus/contact_us.html' , {'form':form , 'sent':sent})
