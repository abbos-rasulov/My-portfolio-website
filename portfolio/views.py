from django.shortcuts import render
from .models import Skill, Service


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
    services = Service.objects.all()
    ctx = {
        'services': services,
    }
    return render(request, 'services.html', ctx)


def resume(request):
    return render(request, 'resume.html')


def works(request):
    return render(request, 'works.html')


def contact(request):
    return render(request, 'contact.html')


def testimonials(request):
    return render(request, 'testimonials.html')