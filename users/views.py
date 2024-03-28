from django.shortcuts import render

# Create your views here.
def userRegister(request):
    return render(request, 'users/register.html')

def userLogin(request):
    return render(request, 'users/login.html')
