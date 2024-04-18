from django.shortcuts import render, redirect
from .forms import RegisterationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def userRegister(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request ,'Something went wrong, Please try again.')
    else:
        form = RegisterationForm()
    return render(request, 'users/register.html', {'form': form})

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    return render(request, 'users/login.html')

def userLogout(request):
    logout(request)
    return redirect('home')
