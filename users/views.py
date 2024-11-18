from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ProfilePictureForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f"User {user.username} created successfully!")
            login(request, user)
           
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required(login_url="/users/login/")
def user_profile(request):
    user=request.user
    form = ProfilePictureForm(instance=user)
    return render(request,'users/profile.html',{'user':user,'form':form})

def user_logout(request):
    logout(request)
    return redirect('/users/login') 


@login_required
def user_list(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


@login_required
def profile_pic(request):
    user = request.user
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/users/profile/')  # Redirect to refresh the page
    else:
        form = ProfilePictureForm(instance=user)

    context = {
        'user': user,
        'form': form,
    }
    return render(request, 'users/profile.html', context)