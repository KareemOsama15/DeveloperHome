from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

def startedPage(request):
    return render(request, 'base/startedPage.html')
