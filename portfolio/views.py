from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.mail import send_mail
from django.db import models


def index(request):
    return render(request, 'index.html')


def welcome(request):
    return render(request, 'welcome.html')


def about(request):
    softskills = SoftSkill.objects.all()
    ctx = {
        'softskills': softskills,
    }
    return render(request, 'about.html', ctx)


def services(request):
    services = Service.objects.all()
    ctx = {
        'services': services,
    }
    return render(request, 'services.html', ctx)


def resume(request):
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    ctx = {
        'educations': educations,
        'experiences': experiences,
    }
    return render(request, 'resume.html', ctx)


def works(request):
    categories = Category.objects.all()
    works = Work.objects.all()
    return render(request,
                  'works.html',
                  {'categories': categories,
                   'works': works})


def contact(request):
    sent = False
    if request.POST:
        model = UserContact()
        model.name = request.POST.get('name', None)
        model.email = request.POST.get('email', None)
        model.subject = request.POST.get('subject', None)
        model.message = request.POST.get('message', None)
        model.created = models.DateTimeField(auto_now_add=True)
        model.updated = models.DateTimeField(auto_now=True)
        model.save()
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = f"{request.POST.get('name')} who is a" \
                  f" {subject} sent you the message : " \
                  f"{request.POST.get('message')} from the mail : {email}"
        send_mail(subject, message, 'abbosr180@gmail.com', [email])
        sent = True
        # ... send email
    return render(request, 'contact.html')


def team(request):
    teammates = Team.objects.all()
    return render(request,
                  'team.html',
                  {"teammates": teammates})
