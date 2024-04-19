from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate , login
from .forms import LoginForm , UserRegistrationForm , UserEditForm , ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request, 'account/register.html' , {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html' , {'user_form':user_form})

        
        



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import UserEditForm, ProfileEditForm
from .models import Profile



@login_required
def dashboard(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # If profile does not exist, create a new one and set the user attribute
        profile = Profile(user=request.user)

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = request.user  # Set the user attribute
            profile.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=profile)

    return render(request, 'account/dashboard.html', {'section': 'dashboard', 'user_form': user_form, 'profile_form': profile_form})



# @login_required
# def edit(request):
#     if request.mehtod == 'POST':
#         user_form = UserEditForm(instance=request.user, date=request.POST)
#         profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST , files=request.FILES)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#     else:
#         user_form = UserEditForm(instance=request.user)
#         profile_form = ProfileEditForm(instance=request.user.profile)
#     return render(request , 'account/dashboard.html' , {'user_form':user_form , 'profile_form':profile_form})
