from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def welcome(request):
    return render(request, 'welcome.html')


def about(request):
    return render(request, 'about.html')
