from django.shortcuts import render
from .models import Skill


def index(request):
    return render(request, 'index.html')


def welcome(request):
    return render(request, 'welcome.html')


def about(request):
    skills = Skill.objects.all()
    ctx = {
        'skills': skills,
    }
    return render(request, 'about.html', ctx)


def services(request):
    return render(request, 'services.html')
