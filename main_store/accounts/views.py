from django.shortcuts import render, redirect
from django.contrib import messages, auth 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import Account
from django.contrib.auth import authenticate , logout
from orders.models import OrderItem

# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()

            # User Activation 
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message = render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)), # Encriypt id for user and decriypt id for user after activation
                'token': default_token_generator.make_token(user), # create token 
            })
            to_email = email
            send_email = EmailMessage(mail_subject , message, to=[to_email])
            send_email.send()
            # messages.success(request , 'Thanks you for register with us. we have send you a varification email to your email address. Please vrifiy it.')
            return redirect('/accounts/login/?command=verification&email='+email)
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)            




def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate( request , email = email , password = password)
        if user is not None:
            auth.login(request , user)
            messages.success(request , 'Your are login now (:')
            return redirect('accounts:dashboard')
        else:
            messages.error(request , 'Invalid Error !')
            return redirect('accounts:login')

    return render(request , 'accounts/login.html')


@login_required(login_url='accounts:login')
def user_logout(request):
    logout(request)
    messages.success(request, 'You are logged out')
    return redirect('accounts:login')



def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('accounts:login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('accounts:register')
    



@login_required(login_url='login') # Not showing dashboard if login is not success
def dashboard(request):
    orders = OrderItem.objects.all()

    return render(request , 'accounts/dashboard.html' , {'orders':orders})




def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            # Reset password email
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Password reset email has been sent to your email address.')
            return redirect('accounts:login')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('accounts:forgotPassword')
    return render(request, 'accounts/forgotPassword.html')



def resetpassword_validate(request , uidb64 , token):
    # check the link is active 
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request , 'Please reset your password')
        return redirect('accounts:resetPassword')
    else:
        messages.error(request , 'This link has been expired !')
        return redirect('accounts:login')
    


def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']
        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request  ,'Password reset successfly')
            return redirect('accounts:login')
        else:    
            messages.error(request , 'Password does not match !')
            return redirect('accounts:resetPassword')
    else:    
       return render(request , 'accounts/resetPassword.html')
    






